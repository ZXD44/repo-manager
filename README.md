# ?? Repo Manager - ��ǨѴ��� GitHub Repository ��� Release

`Repo Manager` ������ͧ��� GUI ����Ѻ�ʡ��ͻ������ҧ���� Python (Tkinter) ���ͪ�������èѴ��� GitHub repository �ͧ�س���¢�� ����ö Push ���������ҧ Release ���������ҧ�дǡʺ�¼�ҹ˹�ҵ�ҧ����������§�������ҹ����


## ? �س���ѵ���ѡ (Features)

- **�ѻ��Ŵ��� (Push):** Push �������¹�ŧ�ҡ����ͧ�ͧ�س��ѧ GitHub repository
- **���ҧ Release:** ���ҧ GitHub Release ���� ������к��й������ѹ�Ѵ�������ҧ Changelog (��¡������¹�ŧ) �ҡ commit ����ش���ѵ��ѵ�
- **�ӷ����� (Do All):** �ѧ��ѹ��������� Push �����С�����ҧ Release ���㹢�鹵͹����
- **��Ǩ�Ѻ�������ѵ��ѵ�:** ��ҹ��������Ңͧ (Owner) ��Ъ��� Repository �ҡ `git remote` ���ਤ�ͧ�س
- **���ҧ Repository ����:** �ҡ Repository �ѧ����պ� GitHub ����ö���ҧ������������ѵ��ѵ� (�� Public)
- **��䫹���§��:** �Ҿ���������������� GitHub ���ѹ����
- **�ѹ�֡��÷ӧҹ (Logging):** �ʴ��š�÷ӧҹ�ء��鹵͹Ẻ Real-time
- **��ʹ���:** �� GitHub Personal Access Token (PAT) 㹡���������͡Ѻ API ��������ѹ�֡ Token �ͧ�س������

## ?? ��觷���ͧ�� (Requirements)

- Python 3.x
- �Դ��� Git ������ͧ����������ͧ�س
- �ź���� `requests` (ʤ�Ի��о������Դ���������ѵ��ѵ�������ѹ�����á)

## ??? ��õԴ���������������ҹ (Installation & Usage)

1.  ��ǹ���Ŵ��� `repo_manager.py`
2.  �Դ Terminal ���� Command Prompt ��������������
3.  �ѹʤ�Ի����¤����:
    ```bash
    python repo_manager.py
    ```
4.  �ҡ�ѧ������ź���� `requests` ʤ�Ի��зӡ�õԴ�������͹����������

## ?? �Ը���ҹ (How to Use)

1.  **��������ਤ:**
    - ���������������Ѩ�غѹ�繤���������
    - ����ö������ **"���͡"** ��������¹��ѧ��������ਤ Git �ͧ�س
    - ������о������֧������ repo �ҡ remote `origin` ���ѵ��ѵ�

2.  **GitHub Token:**
    - �س���繵�ͧ�� Personal Access Token (PAT) ����������������ö������áѺ GitHub ��
    - ������ **"���������"** ���ʹ٢�鹵͹������ҧ Token
    - �� Token ��������ҧ㹪�ͧ **"GitHub Token"**

3.  **������ Repository:**
    - ���� **"��Ңͧ"** ��� **"���� Repository"** �ж١���������ѵ��ѵ� �ҡ���١��ͧ ����ö�������µ��ͧ

4.  **��ô��Թ��� (Actions):**
    - **?? �ѻ��Ŵ���:** �ӡ�� `git add .`, `git commit`, ��� `git push` ��ѧ branch ��ѡ (`main`)
    - **?? ���ҧ Release:** �Դ˹�ҵ�ҧ����Ѻ���ҧ Release ���� �¨��й������ѹ������ҧ Changelog ������ѵ��ѵ� �س����ö�����������´���͹�׹�ѹ
    - **?? �ӷ�����:** �繡�кǹ��� 2 ��鹵͹ ��� "�ѻ��Ŵ���" ��͹ �ҡ��鹨��Դ˹�ҵ�ҧ "���ҧ Release" ������ͧ�ѹ
    - **?? ��Ǩ�ͺ:** �礤����������ҹ�ͧ Git, Token ��� Repository

## ?? �͹حҵ (License)

�鴹������������ MIT License

## ????? ���Ѳ�� (Author)

���ҧ��оѲ���� **ZirconX**