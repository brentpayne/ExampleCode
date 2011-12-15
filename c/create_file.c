
#include <stdio.h>

void main() {
 FILE *fp;
 fp=fopen("/tmp/test.bin", "wb");
 char x[10]="ABCDEFGHIJ";
 int i;
 for(i = 0; i<10000; ++i) {
     fwrite(x, sizeof(x[0]), sizeof(x)/sizeof(x[0]), fp);
 }
 fclose(fp);
}
