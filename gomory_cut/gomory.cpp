#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <dos.h>
#define M 30
#define N 30
double s[N + 2][M + 1], r, gz, t4, t5;
int kgd, kgd2, blap, blap2, sb, cmin, x0, ss;
int m, n, n1, i, j, k, l, le, lc, tg, cs[N + 2], nc[M + 1];
unsigned long far *t;
long int t1, t2;
char *s1, *s2;
FILE *f1, *f2;
int ktnguyen(double x);
int cotquay();
void biendoi();
void inbang(int cuoi);
int dhdoingau();
void main()
{
    clrscr();
    t = (unsigned long far *)MK_FP(0, 0X46C);
    t1 = *t;
    printf("\nCo in trung gian hay khong 1/0 ? ");
    scanf("%d%*c", &tg);
    // Nhap du lieu
    printf("\nVao ten tep so lieu : ");
    gets(s1);
    f1 = fopen(s1, "r");
    fscanf(f1, "%d%d%lf%d%d%d", &n, &m, &gz, &n1, &x0, &ss);
    for (i = 0; i <= n; i++)
        for (j = 0; j <= m; j++)
        {
            fscanf(f1, "%lf", &r);
            s[i][j] = r;
        }
    for (i = 0; i <= n; i++)
        fscanf(f1, "%d", &cs[i]);
    for (j = 1; j <= m; j++)
        fscanf(f1, "%d", &nc[j]);
    fclose(f1);
    sb = 1;
    blap = 0;
    // In du lieu nhap de kiem tra
    printf("\nn,m,gz,n1,x0,ss=%d %d %13.5lf %d %d%d", n, m, gz, n1, x0, ss);
    if (tg == 1)
    {
        printf("\nVao ten tep chua ket qua : ");
        gets(s2);
        f2 = fopen(s2, "w");
        fprintf(f2, "\nn,m,gz,n1,x0,ss=%d%d%13.5lf%d%d%d", n, m, gz, n1, x0, ss);
    }
    printf("\nBang 1, so lieu ban dau");
    if (tg == 1)
        fprintf(f2, "\nBang 1, so lieu ban dau");
    inbang(0);
    if (ss == 1)
    {
        printf("\nBang 1, so lieu ban dau, l- chuan, chap nhan duoc");
        if (tg == 1)
            fprintf(f2, "\nBang 1, so lieu ban dau, l- chuan, chap nhan duoc");
        lc = n;
        goto Lap1;
    }
    if (ss == 2)
    {
        printf("\nBang1,ban dau,l-chuan,khong chap nhan duoc,chay DHDN");
        if (tg == 1)
            fprintf(f2, "\nBang 1,ban dau,l- chuan, khong chap nhan duoc,chay DHDN");
        lc = n;
        goto L1;
    }
    // Them rang buoc phu
    sb = 1;
    cs[n + 1] = n + 1;
    s[n + 1][0] = gz;
    for (j = 1; j <= m; j++)
        s[n + 1][j] = 1;
    printf("\nBang 1, so lieu ban dau them rang buoc phu");
    if (tg == 1)
        fprintf(f2, "\nBang 1,so lieu ban dau them rang buoc phu");
    inbang(1);
    l = n + 1; // dong quay la dong cuoi cung
               // Xac dinh cot quay
    cmin = 1;
    for (j = 2; j <= m; j++)
    {
        for (i = 0; i <= n; i++)
        {
            if (s[i][cmin] > s[i][j])
            {
                cmin = j;
                break;
            }
            if (s[i][cmin] < s[i][j])
                break;
        }
    }
    printf("\nDong quay= %d, Cot quay= %d, Phan tu quay =%13.5lf",
           l, cmin, s[l][cmin]);
    if (tg == 1)
    {
        fprintf(f2, "\nDong quay= %d, Cot quay= %d, Phan tu quay= %13.5lf",
                l, cmin, s[l][cmin]);
    }
    biendoi();
    sb++;
    printf("\nBang %d, l- chuan dau tien", sb);
    if (tg == 1)
        fprintf(f2, "\nBang %d, l- chuan dau tien", sb);
    inbang(0);
    lc = n + 1;
L1:
    kgd2 = dhdoingau();
    if (kgd2 == 1)
    {
        printf("\nBai toan phu khong giai duoc, STOP");
        if (tg == 1)
            fprintf(f2, "\nBai toan phu khong giai duoc,STOP");
        getch();
        getch();
        return;
    }
    // Tim xong bang l- chuan + chap nhan duoc, sang Buoc lap lon
Lap1:
    blap = blap + 1;
    printf("\n------------------------------------------------");
    printf("\n\nBUOC LAP LON THU %d: ", blap);
    if (tg == 1)
    {
        fprintf(f2, "\n---------------------------------------");
        fprintf(f2, "\n\nBUOC LAP LON THU %d: ", blap);
    }
    // Kiem tra loi giai toi uu bai toan phu co nguyen khong
    le = -1;
    for (i = x0; i <= n1; i++)
        if (ktnguyen(s[i][0]) == 0)
        {
            le = i;
            break;
        }
    printf("\nThanh phan le thuoc dong = %d", le);
    if (tg == 1)
        fprintf(f2, "\nThanh phan le thuoc dong = %d", le);
    if (le == -1)
    {
        printf("\nPHUONG AN TOI UU QHTT NGUYEN: ");
        if (tg == 1)
            fprintf(f2, "\nPHUONG AN TOI UU QHTT NGUYEN: ");
        for (i = 0; i <= n; i++)
            printf("\nx[%2d] = %13.5lf", cs[i], s[i][0]);
        printf("\nSo luong lat cat: %d lat cat", blap - 1);
        printf("\nSo bang don hinh da lap : %d bang", sb);
        if (tg == 1)
        {
            for (i = 0; i <= n; i++)
                fprintf(f2, "\nx[%2d] = %13.5lf", cs[i], s[i][0]);
            fprintf(f2, "\nSo luong lat cat: %d lat cat", blap - 1);
            fprintf(f2, "\nSo bang don hinh da lap : %d bang", sb);
        }
        t = (unsigned long far *)MK_FP(0, 0X46C);
        t2 = *t;
        printf("\nThoi gian chay chuong trinh: %ld giay",
               (long int)((t2 - t1) / 18.21));
        if (tg == 1)
            fprintf(f2, "\nThoi gian chay chuong trinh:%ld giay",
                    (long int)((t2 - t1) / 18.21));
        fclose(f2);
        getch();
        return;
    }
    // Tao lat cat moi va ghi vao cuoi bang
    lc++;
    cs[n + 1] = lc;
    s[n + 1][0] = -(s[le][0] - floor(s[le][0]));
    for (j = 1; j <= m; j++)
        if (nc[j] <= n1)
        { // khi xj <= n1
            if (ktnguyen(s[le][j]))
                s[n + 1][j] = 0;
            else
            {
                if ((s[le][j] - floor(s[le][j])) <= fabs(s[n + 1][0]))
                    s[n + 1][j] = -(s[le][j] - floor(s[le][j]));
                else
                    s[n + 1][j] = -(fabs(s[n + 1][0]) / (1 - fabs(s[n + 1][0]))) * (1 - (s[le][j] - floor(s[le][j])));
            }
        } // khi xj > n1
        else
        {
            if (s[le][j] < 0)
                s[n + 1][j] = -(fabs(s[n + 1][0]) / (1 - fabs(s[n + 1][0]))) * (-s[le][j]);
            else
                s[n + 1][j] = -s[le][j];
        }
    printf("\nBang %d, sau khi them lat cat", sb);
    if (tg == 1)
        fprintf(f2, "\nBang %d, sau khi them lat cat", sb);
    inbang(1);
    // Xac dinh dong quay va cot quay
    l = n + 1;
    printf("\nDong quay = %d", l);
    if (tg == 1)
        fprintf(f2, "\nDong quay = %d", l);
    cotquay();
    printf("\nCot quay = %d, Phan tu quay = %13.5lf", cmin, s[l][cmin]);
    if (tg == 1)
        fprintf(f2, "\nCot quay=%d,Phan tu quay=%13.5lf", cmin, s[l][cmin]);
    // Bien doi bang don hinh
    biendoi();
    sb++;
    printf("\nBang %d, bang dau tien bai toan phu", sb);
    if (tg == 1)
        fprintf(f2, "\nBang %d, bang dau tien bai toan phu", sb);
    inbang(0);
    kgd2 = dhdoingau();
    if (kgd2 == 1)
    {
        printf("\nBai toan phu khong giai duoc");
        if (tg == 1)
            fprintf(f2, "\nBai toan phu khong giai duoc, STOP");
        getch();
        getch();
        return;
    }
    goto Lap1;
}
int ktnguyen(double x)
{
    long int h;
    double z;
    z = fabs(x);
    h = (int)(z + 0.5);
    if (fabs(z - h) <= 0.0001)
        return 1;
    else
        return 0;
}
int cotquay()
{
    k = 0;
    for (j = 1; j <= m; j++)
        if (s[l][j] < -0.000001)
        {
            k = j;
            break;
        }
    if (k == 0)
        return 1;
    cmin = k;
    for (j = k + 1; j <= m; j++)
        if (s[l][j] < -0.000001)
        {
            for (i = 0; i <= n; i++)
            {
                t4 = s[i][cmin] / fabs(s[l][cmin]);
                t5 = s[i][j] / fabs(s[l][j]);
                if (t4 > t5)
                {
                    cmin = j;
                    break;
                }
                if (t4 < t5)
                    break;
            }
        }
    return 0;
}
void biendoi()
{
    for (j = 0; j <= m; j++)
        if (j != cmin)
        {
            for (i = 0; i <= n; i++)
                if (i != l)
                    s[i][j] = s[i][j] - (s[l][j] / s[l][cmin]) * s[i][cmin];
            s[l][j] = 0;
        }
    for (i = 0; i <= n; i++)
        if (i != l)
            s[i][cmin] = -s[i][cmin] / s[l][cmin];
    s[l][cmin] = -1;
    nc[cmin] = cs[l];
}
void inbang(int cuoi)
{
    int n1;
    if (cuoi == 1)
        n1 = n + 1;
    else
        n1 = n;
    printf("\nCo so : ");
    for (i = 0; i <= n1; i++)
        printf("%d ", cs[i]);
    printf("\n");
    printf("Phi co so : ");
    for (j = 1; j <= m; j++)
        printf("%d ", nc[j]);
    printf("\n");
    for (i = 0; i <= n1; i++)
    {
        for (j = 0; j <= m; j++)
            printf(" %10.5lf ", s[i][j]);
        printf("\n");
    }
    if (tg == 1)
    {
        fprintf(f2, "\nCo so : ");
        for (i = 0; i <= n1; i++)
            fprintf(f2, "%d ", cs[i]);
        fprintf(f2, "\n");
        fprintf(f2, "Phi co so : ");
        for (j = 1; j <= m; j++)
            fprintf(f2, "%d ", nc[j]);
        fprintf(f2, "\n");
        for (i = 0; i <= n1; i++)
        {
            for (j = 0; j <= m; j++)
                fprintf(f2, " %13.5lf ", s[i][j]);
            fprintf(f2, "\n");
        }
    }
    getch();
}
int dhdoingau()
{
    blap2 = 0;
Lap2:
    blap2++;
    printf("\nBuoc lap Don hinh doi ngau thu %d : ", blap2);
    if (tg == 1)
        fprintf(f2, "\nBuoc lap Don hinh doi ngau thu %d :", blap2);
    l = -1;
    for (i = 1; i <= n; i++)
        if (s[i][0] < 0)
        {
            l = i;
            break;
        }
    printf("\nDong quay %d ", l);
    if (tg == 1)
        fprintf(f2, "\nDong quay = %d", l);
    if (l == -1)
    {
        printf("\nBang tren ung phuong an toi uu cua bai toan phu");
        if (tg == 1)
            fprintf(f2, "\nBang tren ung phuong an toi uu bai toan phu");
        return 0;
    }
    else
    {
        kgd = cotquay();
        if (kgd == 1)
            return 1;
        printf("\nCot quay=%d, Phan tu quay=%13lf", cmin, s[l][cmin]);
        if (tg == 1)
            fprintf(f2, "\nCot quay = %d, Phan tu quay =%13.5lf",
                    cmin, s[l][cmin]);
        biendoi();
        sb++;
        printf("\nBang %d, DHDN", sb);
        if (tg == 1)
            fprintf(f2, "\nBang %d, DHDN", sb);
        inbang(0);
        goto Lap2;
    }
}