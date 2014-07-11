package algorithm;

import java.util.Random;

public class SkipList {
	
	private static int MAX_HEIGHT = 32;

	private class Node {
		
		int value;
		
		Node next[];
		
		public Node(int value) {
			this.value = value;
			this.next = new Node[MAX_HEIGHT];
		}
	}
	
	private int level = 1;
	
	private Node head = new Node(0);
	
	private Random random = new Random();
	
	public void insert(int value) {
		// generate a level for the new inserted node
		int newNodeLevel = 0;
		for (int R = random.nextInt(); (R & 1) == 1; R >>= 1) {
			newNodeLevel++;
			if (newNodeLevel == this.level) {
				if (this.level < MAX_HEIGHT) {
					this.level++;
				}
				
				break;
			}
		}
		
		Node newNode = new Node(value);
		
		Node cur = this.head;
		for (int i = this.level - 1; i >= 0; i--) {
			// walk though the list at level i.
			// if cur.next[i] is greater than the value, it
			// denotes that we should stop walking.
			for (; cur.next[i] != null; cur = cur.next[i]) {
				if (cur.next[i].value > value) {
					break;
				}
			}
			
			// current level is lower than newNodeLevel.
			// we insert new node into the current level list. 
			if (i <= newNodeLevel) {
				newNode.next[i] = cur.next[i];
				cur.next[i] = newNode;
			}
		}
	}
	
	public boolean contain(int value) {
		Node cur = this.head;
		for (int i = this.level - 1; i >= 0; i--) {
			for (; cur.next[i] != null; cur = cur.next[i]) {
				// go to the lower level.
				if (cur.next[i].value > value) {
					break;
				}
				
				if (cur.next[i].value == value) {
					return true;
				}
			}
		}
		return false;
	}
	
	public boolean delete(int value) {
		boolean found = false;
		
		Node cur = this.head;
		for (int i = this.level - 1; i >= 0; i--) {
			for (; cur.next[i] != null; cur = cur.next[i]) {
				// go to the next lower level.
				if (cur.next[i].value > value) {
					break;
				}
				
				// found the node in the current level.
				// delete the node.
				// then go to the next lower level.
				if (cur.next[i].value == value) {
					cur.next[i] = cur.next[i].next[i];
					found = true;
					break;
				}
			}
		}
		
		return found;
	}
	
	public static void main(String[] args) {
		
		SkipList list = new SkipList();
		
		int NUM = 1000000;
		
		for (int i = 0; i < NUM; i++) {
			list.insert(i);
		}
		
		for (int i = 0; i < NUM; i++) {
			if (!list.contain(i)) {
				System.out.println("error");
			}
		}
		
		for (int i = 0; i < NUM; i++) {
			list.delete(i);
		}
		
		for (int i = 0; i < NUM; i++) {
			if (list.contain(i)) {
				System.out.println("error");
			}
		}
		
	}
}
