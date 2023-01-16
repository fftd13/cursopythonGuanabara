larg=float(input('largura da parede:'))
alt=float(input('altura da parede:'))
area=larg*alt
l=area/2
print('sua area tem a dimençao de {}mx{}m e sua area é de {}m²'.format(larg,alt,area))
print('voce precisa de {:.3f}L de tinta para cobrir uma area de {}m²'.format(l,area))