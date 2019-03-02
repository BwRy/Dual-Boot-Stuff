CC=gcc

ida_patcher:
	$(CC) ida_patcher.c -o ida_patcher
imagine:
	$(CC) imagine.c -o imagine
reimagine:
	$(CC) -o reimagine
image3maker:
	$(CC) image3maker.c -O2 -pipe -o image3maker
iBoot32Patcher:
	$(CC) *.c -Wno-multichar -I. -o iBoot32Patcher
CBPatcher:
	$(CC) *.c -o CBPatcher
clean:
	rm -f *.o
