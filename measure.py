import subprocess,time,json,os,sys
import requests,pandas as pd,numpy as np
from load_test import run
PY=sys.executable
URL='http://127.0.0.1:8000/v1/models/eta:predict'
rows=pd.read_csv('data/eta_fresh.csv').head(200)
rows=rows[['distance_km','n_stops','hour','weekday','traffic_index','rain','weight_kg']]
rows.to_csv('data/eta_sample.csv',index=False)
rows=rows.to_dict('records')
def wait(url):
    for _ in range(120):
        try:
            if requests.get(url,timeout=1).status_code==200:return
        except requests.RequestException:pass
        time.sleep(.5)
    raise RuntimeError('server startup timeout '+url)
def server(workers):
    p=subprocess.Popen([PY,'-m','uvicorn','partA.eta_app:app','--host','127.0.0.1','--port','8000','--workers',str(workers),'--no-access-log'],stdout=open(f'uvicorn{workers}.log','w'),stderr=subprocess.STDOUT,start_new_session=True)
    wait('http://127.0.0.1:8000/healthz');return p
def stop(p):
    import signal
    os.killpg(p.pid,signal.SIGTERM);p.wait(timeout=30)
p=server(1)
try:
    results=[run(URL,'rest',c,4,rows,1) for c in [1,2,4,8,16]]
    json.dump(results,open('partA/loadtest_results.json','w'),indent=2)
    print(pd.DataFrame(results).to_string(index=False),flush=True)
    batch=[]
    for n in [1,100]:
        s=requests.Session(); times=[]
        for _ in range(200):
            t=time.perf_counter();r=s.post(URL,json={'instances':rows[:n]},timeout=30);r.raise_for_status();times.append((time.perf_counter()-t)*1000/n)
        batch.append({'batch':n,'mean_ms_per_row':float(np.mean(times))})
    json.dump(batch,open('partA/batch_results.json','w'),indent=2);print('batch:',batch,flush=True)
    subprocess.run([PY,'partD/smoke_eta.py','--url',URL,'--expect-version','v1'],check=True)
finally:stop(p)
p=server(2)
try:
    improved=[run(URL,'rest',c,4,rows,1) for c in [1,2,4,8,16]]
    json.dump(improved,open('partA/two_workers_results.json','w'),indent=2);print('TWO WORKERS\n',pd.DataFrame(improved).to_string(index=False),flush=True)
finally:stop(p)
