#include <iostream>
#include <string>
using namespace std;

struct Ngay{
    int ngay, thang, nam ;
};
struct SinhVien{
    int ma;
    Ngay ngay_sinh;
    string ten;
    string gioi_tinh;
    string dia_chi;
    string lop;
    string khoa;
};

struct Node{
    SinhVien *data;
    Node *link;
};
struct SingleList{
    Node *first;
};
//khoi tao danh sach 
void Initialize(SingleList *&list){
    list = new SingleList;
    list->first = NULL;
}
//nhap thong tin sinh vien
SinhVien *NhapSinhVien()
{
    SinhVien *sv = new SinhVien;
    cout<<"Nhap MSSV: "; cin>>sv->ma;
    cout << "Nhap ngay, thang, nam sinh : " ; 
    cin >> sv->ngay_sinh.ngay >> sv->ngay_sinh.thang >> sv->ngay_sinh.nam;

    cin.ignore();
    cout<<"Nhap ho va ten: "; getline(cin,sv->ten);

    cout<<"Nhap gioi tinh: "; getline(cin,sv->gioi_tinh);

    cout<<"Nhap lop: "; getline(cin,sv->lop);

    cout<<"Nhap khoa: "; getline(cin,sv->khoa);

    cout<<"Nhap dia chi: "; getline(cin,sv->dia_chi);
    return sv;
}
//tao node sinh vien
Node *CreateNode(SinhVien *sv)
{
    Node *pNode = new Node;
    if(pNode!=NULL)
    {
        pNode->data=sv;
        pNode->link=NULL;
    }
    else
    {
        cout<<"Update fail";
    }
    return pNode;
}
//them node vao cuoi danh sach
void InsertLast(SingleList *&list,SinhVien *sv)
{
    Node *pNode=CreateNode(sv);
    if(list->first==NULL)
    {
        list->first=pNode;
    }
    else
    {
        Node *temp=list->first;
         
        while(temp->link!=NULL)
        {
            temp=temp->link;
        }
        temp->link=pNode;
    }
}
//hien thi danh sach
void PrintList(SingleList *list)
{
    Node *temp = list->first;
    if(temp==NULL)
    {
        cout<<"Danh sach rong";
        return;
    }
    while(temp!=NULL)
    {
        SinhVien *sv=temp->data;
        cout<<sv->ma<<"\t"<<sv->ten<<endl;
        temp=temp->link;
    }
}
//sap xep
void SortList(SingleList *&list)
{
    for(Node *temp=list->first;temp!=NULL;temp=temp->link)
    {
        for(Node *temp2=temp->link;temp2!=NULL;temp2=temp2->link)
        {   
            SinhVien *svTmp=temp->data;
            SinhVien *svTmp2=temp2->data;
            if(svTmp2->ma<svTmp->ma)
            {
                int ma = svTmp->ma;
                int ngay, thang, nam;
                ngay = svTmp->ngay_sinh.ngay;
                thang = svTmp->ngay_sinh.thang;
                nam = svTmp->ngay_sinh.nam;

                string ten; ten = svTmp->ten;
                string lop; lop = svTmp->lop;
                string khoa; khoa = svTmp->khoa;
                string dia_chi; dia_chi = svTmp->dia_chi;
                string gioi_tinh; gioi_tinh = svTmp->gioi_tinh;

                 
                svTmp->ma = svTmp2->ma;
                svTmp->ten = svTmp2->ten;
                svTmp->ngay_sinh.ngay = svTmp2->ngay_sinh.ngay;
                svTmp->ngay_sinh.thang = svTmp2->ngay_sinh.thang;
                svTmp->ngay_sinh.nam = svTmp2->ngay_sinh.nam;
                svTmp->lop = svTmp2->lop;
                svTmp->khoa = svTmp2->khoa;
                svTmp->dia_chi = svTmp2->dia_chi;
                svTmp->gioi_tinh = svTmp2->gioi_tinh;

                svTmp2->ma=ma;
                svTmp2->ten=ten;  
                svTmp2->ngay_sinh.ngay=ngay;
                svTmp2->ngay_sinh.thang=thang;
                svTmp2->ngay_sinh.nam=nam;
                svTmp2->lop=lop;
                svTmp2->khoa=khoa;
                svTmp2->dia_chi=dia_chi;
                svTmp2->gioi_tinh=gioi_tinh;
                          
            }
        }   
    }
}
//xoa
void RemoveNode(SingleList *&list,int ma)
{
    Node *pDel=list->first;
    if(pDel==NULL)
    {
        cout<<"Danh sach rong!";
    }
    else
    {
        Node *pPre=NULL;
        while(pDel!=NULL)
        {
            SinhVien *sv=pDel->data;
            if(sv->ma==ma)
                break;
            pPre=pDel;
            pDel=pDel->link;
        }
        if(pDel==NULL)
        {
            cout<<"khong tim thay MSSV: "<<ma;
        }
        else
        {
            if(pDel==list->first)
            {
                list->first=list->first->link;
                pDel->link=NULL;
                delete pDel;
                pDel=NULL;
            }
            else
            {
                pPre->link=pDel->link;
                pDel->link=NULL;
                delete pDel;
                pDel=NULL;
            }
        }
    }
}
int main() {
    SingleList *list;
    Initialize(list);

    do{
        SinhVien *sv = NhapSinhVien();
        InsertLast(list,sv);
        cout << "Nhap 1 de tiep tuc ; 0 de ket thuc : " ;
        bool check; cin >> check; 
        if(check == 0 ) break;
    }while(true);
    PrintList(list);
    SortList(list);
    cout<<"\nSau khi sap xep:\n";
    PrintList(list);
    cout<<"\nBan muon xoa sinh vien co MSSV: ";
    int ma; cin>>ma;
    RemoveNode(list,ma);
    cout<<"\nSau khi xoa:\n";
    PrintList(list);
 
}
