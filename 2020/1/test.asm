section	.data
m	db 'Hello world!',10

section	.text
	global _start 

_start:
	mov ecx, m
	mov edx, 13
	mov eax, 4
	mov ebx, 1
	int 80h

	mov eax, 1
	mov ebx, 0
	int 80h