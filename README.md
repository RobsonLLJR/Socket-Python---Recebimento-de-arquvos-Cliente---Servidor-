# Socket-Python---Recebimento-de-arquvos-Cliente---Servidor-

Utilização de socket na linguagem de programação python em que se faz a iniciação do servidor no localhost e com isso é feito o pedido de acesso do cliente na porta do servidor.


Socket
O modulo socket prove interfaces de socket BSD, disponiveis em praticamente todos os sistemas operacionais.

Familias de sockets
Diversas famílias de sockets podem ser usadas para termos acessos a objetos que nos permitam fazer chamadas de sistema. Nesse exemplo usei a AF_INET.

AF_INET precisa basicamente de um par de dados, contendo um endereço IPv4 e uma porta para ser instanciada. Para endereços IPv6 o modulo disponibiliza o AF_INET6

Constante [SOCK_STREAM]
As constantes representam as famílias de sockets, como a constante AF_INET e os protocolos usados como parâmetros para o modulo socket. 
Um dos protocolos mais usados encontrados na maioria dos sistemas é o SOCK_STREAM.

Ele é um protocolo baseado em comunicação que permite que duas partes estabeleçam uma conexão e conversem entre si.
