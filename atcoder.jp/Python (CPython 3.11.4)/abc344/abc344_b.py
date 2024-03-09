import sys

r = sys.stdin.buffer.read()
a = r.split(b'\n')
a.reverse()
sys.stdout.buffer.write(b'\n'.join(a))
