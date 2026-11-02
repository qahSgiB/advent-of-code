default rel



section	.data
nl	db 0ah,'$'
vstr	db "1721",0ah,"979",0ah,"366",0ah,"299",0ah,"675",0ah,"1456",'$'
v	resw 100
vindex	dw 0
vlength	dw 0
ostr	resb 100
oindex	dw 0
olength	dw 0
ostr1	resb 100

section	.text
	global _start 

_start	mov ax, 0
	mov cx, 0
	
l0start	mov rbx, 0
	mov bx, cx
	mov dl, [vstr+rbx]
	
	cmp dl, '$'
	jz l0out
	
	cmp dl, 0ah
	jz iffer1
	jmp iffer2
	
iffer2	jmp aiffer
	
iffer1	call addv

	mov ax, cx
	inc ax
	
aiffer	inc cx
	
	jmp l0start
	
l0out	call addv

	mov ax, [vindex]
	mov [vlength], ax
	mov word[vindex], 0
	
	mov cx, 0
	
l2start	mov dx, [vlength]
	cmp cx, dx
	jz l2out
	
	mov si, cx
	inc si
	inc si
	
l3start	mov dx, [vlength]
	cmp si, dx
	jz l3out
	
	mov ax, 0
	
	mov rbx, 0
	mov bx, cx
	add ax, [v+rbx]
	
	mov rbx, 0
	mov bx, si
	add ax, [v+rbx]
	
	mov bx, 2020
	cmp ax, bx
	jz l2out
	
	inc si
	inc si
	jmp l3start
	
l3out	inc cx
	inc cx
	jmp l2start
	
l2out	mov rbx, 0
	mov bx, cx
	mov ax, [v+rbx]
	mov rbx, 0
	mov bx, si
	mov cx, [v+rbx]
	mul cx
	
	mov bx, 10000
	div bx
	
	push ax
	mov ax, dx
	call conv
	pop ax
	call conv
	
	mov bx, [oindex]
	mov [olength], bx
	mov word[oindex], 0
	
	mov cx, 0
	
l5start	mov bx, [olength]
	cmp cx, bx
	jz l5out
	
	mov rbx, 0
	mov bx, [olength]
	dec bx
	sub bx, cx
	mov al, [ostr+rbx]
	
	mov rbx, 0
	mov bx, cx
	mov [ostr1+rbx], al
	
	inc cx
	jmp l5start
	
l5out	mov rbx, 0
	mov bx, cx
	mov byte[ostr1+rbx], 10

	add rbx, 1

	mov ecx, ostr1
	mov edx, ebx
	mov eax, 4
	mov ebx, 1
	int 80h
	
	; mov dx, ostr1
	; mov ah, 9
	; int 21h

	mov eax, 1
	mov ebx, 0
	int 80h
	
conv	mov dx, 0
	
l4start	mov bx, 0
	cmp ax, bx
	jz l4out
	
	mov dx, 0
	mov bx, 10
	div bx
	
	add dx, 48
	
	mov rbx, 0
	mov bx, [oindex]
	mov [ostr+rbx], dl
	inc bx
	mov [oindex], bx
	
	jmp l4start

l4out	ret
	
addv	push cx

	mov si, 1
	mov dx, 0

l1start	cmp cx, ax
	jz l1out

	dec cx
	
	push dx
	push ax
	mov rbx, 0
	mov bx, cx
	mov dl, [vstr+rbx]
	mov al, dl
	sub al, 48
	cbw
	mov bx, ax
	pop ax
	pop dx
	
	push ax
	push dx
	mov ax, bx
	mul si
	mov bx, ax
	pop dx
	pop ax
	
	add dx, bx
	
	push ax
	push dx
	mov ax, si
	mov bx, 10
	mul bx
	mov si, ax
	pop dx
	pop ax
	
	jmp l1start
	
l1out	mov rbx, 0
	mov bx, [vindex]
	mov [v+rbx], dx
	
	inc bx
	inc bx
	mov [vindex], bx

	pop cx
	ret