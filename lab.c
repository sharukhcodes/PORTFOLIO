
#include <stdio.h>
int n=0;
void create(int a[])
{
    int i;
    printf("enter size of array\n");
    scanf("%d",&n);
    printf("enter array elements\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    if(i>0 && a[i]<a[i-1])
    {
        printf("pls enter a value=%d",a[i-1]);
        i--;
    }

}
void display(int a[])
{
    if(n==0)
    {
        printf("\nthe array has no elemts\n");
        return ;
    }
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d",a[i]);
    }
}
void insert (int a[])
{
    int ele,pos=n,i;
    printf("enter the element to be inserted\n");
    scanf("%d",&ele);
    for(i=0;i<n;i++)
    {
    if(a[i]>ele)
    {
        pos=i;
        break;
    }}
    for(i=n;i>pos;i--)
    {
        a[i]=a[i-1];
        a[pos]=ele;
        n++;
    }
    printf("elements inserted successfully\n");
}
void delete(int a[])
{
    if(n==0)
    {
        printf("\nthe array has no elemts\n");
    }
    int ele,pos=-1,i;
      printf("enter the element to be deleted\n");
    scanf("%d",&ele);
    for(i=0;i<n;i++)
    {
    if(a[i]==ele)
    {
        pos=i;
        break;
    }
}
    for(i=pos;i<n-1;i++)
    {
        a[i]=a[i+1];
       n--;
    }
    printf("the element is deleted\n");
}



int main() {
    
    int choice,a[20];
    while(1)
    {
        printf("\n ordered pair");
        printf("\n1 creation");
        printf("\n2 insert");
        printf("\n3 deletion");
        printf("\n4 display");
        printf("\n5 exit\n");
        printf("enter any choice");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:create (a);
            break;
            case 2:insert(a);
            break;
            case 3:delete (a);
            break;
            case 4:display (a);
            break;
            case 5:return 0;
            
            default:printf("invalid choice");
        }
    }
}