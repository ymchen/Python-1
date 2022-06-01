"""Write a function in python to count the number of lowercase
alphabets present in a text file “happy.txt"""


def lowercase():
    with open("happy.txt") as F:
        count_lower = 0
        count_upper = 0
        value = F.read()
        for i in value:
            if i.islower():
                count_lower += 1
            elif i.isupper():
                count_upper += 1
        print("The total number of lower case letters are", count_lower)
        print("The total number of upper case letters are", count_upper)
        print("The total number of letters are", count_lower + count_upper)

if __name__ == "__main__":
    lowercase()


select * from tmp_b_bas_company_add;


SELECT
        DISTINCT issue_org_id,
        thscode,
        tt.org_name_cn
    FROM
        sec_basic_info t
    LEFT JOIN corp_basic_info tt ON
        t.issue_org_id = tt.org_id
    WHERE
        sec_type = 'A股'
        AND is_listing = 1
        and org_name_cn = '观典防务技术股份有限公司'