import os, subprocess

def cv('envname'):
  if not os.path.exists(envname): os.makedirsmakedirs(envname)
  subprocess.run(['python', '-m', 'venv'])

envname = 'myenv'
cv(envname)
