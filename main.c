#include<stdio.h>
#include "bundle.h"
#include <openssl/ssl.h>
int main()
{

bundle *b=bundle_create();
char *popup_timeout;
scanf("%c",&popup_timeout);

char appSysName[]="alert intermediate level";
bundle_add(b,"type","B");
bundle_add(b,"title","System start");
bundle_add(b,"text","Welcome User");

if(atoi(popup_timeout)>0)
{
printf("Timeout is "%s",popup_timeout);
bundle_add(b,"timeout",popup_timeout);
}

if(syspopup_launch(appSysName,b)<0)
printf("Failed to launch syspopup-Start again");
return b;
bundle_free(b);
}

