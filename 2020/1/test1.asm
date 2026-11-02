section .data
f	db 'test_input.txt',0

section .bss
text	resb 20

section .text
global _start

_start	mov rax, 5
	mov rdi, f
	mov rsi, 0
	mov rdx, 0
	syscall

	push rax
	mov rdi, rax
	mov rax, 0
	mov rsi, text
	mov rdx, 15
	syscall

	mov rax, 3
	pop rdi
	syscall

	mov ecx, text
	mov edx, 10
	mov eax, 4
	mov ebx, 1
	int 80h

	mov eax, 1
	mov ebx, 0
	int 80h