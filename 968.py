def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            
            ret = Solution().minCameraCover(root)

            out = str(ret) 
            print(out)
        except StopIteration:
            break

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = 0
    def helper(self, node):
        if node is None:
            return True
        if node.val == 1:
            return True
        if node.left is None and node.right is None:
                return False
        if node.right is None:
            if node.left.val == 0:
                return False
            else:
                return True
        if node.left is None:
            if node.right.val == 0:
                return False
            else:
                return True
        if node.left.val == 0 and node.right.val == 0:
            return False
        else:
            return True
        
    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.right)
        self.dfs(node.left)
        fright = self.helper(node.right)
        fleft = self.helper(node.left)
        if not fright or not fleft:
            node.val = 1
            self.res += 1
            return

        
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root and root.right is None and root.left is None:
            return 1
        if root:
            self.dfs(root)
            if not self.helper(root):
                root.val = 1
                self.res += 1
            return self.res
        else:
            return 0

if __name__ == '__main__':
    main()