/**
 * Binary Search Tree
 * A basic BST supporting insert and search, demonstrating recursive tree
 * traversal and OOP structure (Node as an inner class).
 *
 * Time: O(log n) average for insert/search, O(n) worst case (unbalanced)
 * Space: O(n)
 */
public class BinarySearchTree {
    private Node root;

    private static class Node {
        int value;
        Node left, right;
        Node(int value) { this.value = value; }
    }

    public void insert(int value) {
        root = insertRecursive(root, value);
    }

    private Node insertRecursive(Node node, int value) {
        if (node == null) return new Node(value);
        if (value < node.value) {
            node.left = insertRecursive(node.left, value);
        } else if (value > node.value) {
            node.right = insertRecursive(node.right, value);
        }
        return node;
    }

    public boolean contains(int value) {
        return containsRecursive(root, value);
    }

    private boolean containsRecursive(Node node, int value) {
        if (node == null) return false;
        if (node.value == value) return true;
        return value < node.value
                ? containsRecursive(node.left, value)
                : containsRecursive(node.right, value);
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        int[] values = {8, 3, 10, 1, 6, 14, 4, 7};
        for (int v : values) tree.insert(v);

        System.out.println(tree.contains(6));   // true
        System.out.println(tree.contains(99));  // false
    }
}
