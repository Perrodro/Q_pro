import subprocess

youtubedl_procs = []
urls = ['https://www.youtube.com/watch?v=6Irus3d5f0E', 'https://www.youtube.com/watch?v=PQTZN1fbSgg']

# Crea todos los subprocesos pero sin esperarlos
for url in urls:
    youtubedl_procs.append(subprocess.Popen(['youtube-dl', url]))

# Espera a cada uno de los procesos antes creados
for proc in youtubedl_procs:
    proc.communicate()
