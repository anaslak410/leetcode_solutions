class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"""value: {self.val}
                    next: {self.next}"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_num = self.list_to_num(l1)
        second_num = self.list_to_num(l2)
        print(first_num + second_num)
        return self.num_to_list(first_num + second_num)

    def list_to_num(self, list_node):
        normal_list = ""
        while True:
            normal_list = f"{normal_list}{list_node.val}"
            if list_node.next is None:
                break
            list_node = list_node.next

        print(normal_list)
        return int(normal_list[::-1])

    def num_to_list(self, result):
        num_string = str(result)[::-1]

        list_node = ListNode(val=int(num_string[0]))
        current_node = list_node
        for char in num_string[1:]:
            current_node.next = ListNode(val=int(char))
            current_node = current_node.next

        print(list_node)
        return list_node


if __name__ == '__main__':
    sol = Solution()

    l1Nums = [2, 4, 3]
    l1 = ListNode(l1Nums[0], next=ListNode(
        l1Nums[1], next=ListNode(l1Nums[2])))

    l2nums = [5, 6, 4]
    l2 = ListNode(l2nums[0], next=ListNode(
        l2nums[1], next=ListNode(l2nums[2])))

    print(l1.__str__())
    print(l2.__str__())
    sol.addTwoNumbers(l1, l2)

    l = [1, 2, 3]

    res = [int(item) for item in l]

    print(res)
