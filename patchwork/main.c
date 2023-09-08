#include <stdio.h>


int main() {
    char *v0; // rax
    char *v1; // rax
    __int64 result; // rax
    char s[8]; // [rsp+0h] [rbp-30h] BYREF
    __int64 v4; // [rsp+8h] [rbp-28h]
    __int64 v5; // [rsp+10h] [rbp-20h]
    __int16 v6; // [rsp+18h] [rbp-18h]
    char v7; // [rsp+1Ah] [rbp-16h]
    char *v8; // [rsp+20h] [rbp-10h]
    char *v9; // [rsp+28h] [rbp-8h]

    long int s = 0x9DC59ACB96A493A0LL;
    v4 = 0xB4BE84AFA0C5AFC0LL;
    v5 = 0xA780B4AFC483B7AFLL;
    v6 = -12866;
    v7 = 0;
    v9 = s;
    while ( *v9 )
    {
        v0 = v9++;
        *v0 -= 80;
    }
    puts(s);
    v8 = s;
    while ( 1 )
    {
        result = (unsigned __int8)s*v8;
        v1 = v8++;
        *v1 += 80;
    }
    return result;
}