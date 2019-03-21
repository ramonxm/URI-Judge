def conv(horario):
    h, m = horario.split(':')
    return int(h)*60 + int(m)
    
pa, cb, pb, ca = map(conv,input().split())

duracao = cb + ca - (pa + pb)
duracao = duracao % (60*24)
duracao //= 2

fuso = (cb - (pa + duracao))//60
while fuso < -11:
    fuso += 24
while fuso > 12:
    fuso -= 24
    
print(duracao,fuso)
