# Python Class

class Artifact:
    def __init__(self, name, artifact_set, stat):
        self.name = name
        self.stat = stat
        self.artifact_set = artifact_set

    def display(self):
        return self.name + ' - ' + self.artifact_set + ' - ' + self.stat


def run01():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    print(plume_of_death.display())


# Linked List of String

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def append(self, node):
        if self.first_node is None:
            self.first_node = node
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                current_node = current_node.next

            current_node.next = node
        self.size += 1

    def list(self):
        result = ''
        if self.first_node is None:
            result = 'Empty LinkedList'
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                result = result + current_node.value + ', '
                current_node = current_node.next
            result = result + current_node.value
        return result

def run02():
    my_linked_list = LinkedList()
    node01 = Node('Raiden Shogun')
    node02 = Node('Venti')
    node03 = Node('Barbara')

    my_linked_list.append(node01)
    my_linked_list.append(node02)
    my_linked_list.append(node03)

    print(my_linked_list.list())
    print(my_linked_list.size)


#LinkedList of Artifact


class NodeArtifact:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedListArtifact:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def append(self, node):
        if self.first_node is None:
            self.first_node = node
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                current_node = current_node.next

            current_node.next = node
        self.size += 1

    def list(self):
        result = ''
        if self.first_node is None:
            result = 'Empty Artifact Lists'
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                result = result + current_node.value.name + ', '
                current_node = current_node.next
            result = result + current_node.value.name
        return result


def run03():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    sands_of_eon = Artifact('Sands of Eon', "Noblesse Oblige", 'Element Mastery')

    my_linkedlist = LinkedListArtifact()
    node_artifact01 = NodeArtifact(plume_of_death)
    node_artifact02 = NodeArtifact(sands_of_eon)

    my_linkedlist.append(node_artifact01)
    my_linkedlist.append(node_artifact02)

    print(my_linkedlist.list())



def run():
    # run01()
    # run02()
    run03()
