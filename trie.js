class TrieNode {
    constructor(letter = ''){
        this.val = letter
        this.children = {};
        this.completesString = false;
    }
}

class Trie {
    constructor(){
        this.rootNode = new TrieNode();
    }
    insert(word){
        var node = this.rootNode();

        for(var i=0; i<word.length; i++){
            var currentLetter = word[i];

            if(node.children[currentLetter]){
                node = node.children[currentLetter]
            } else{
                var newNode = new TrieNode(currentLetter);
                node.children[currentLetter] = newNode;
                node = newNode;
            }
        }
        node.completesString = true;
    }
// word what will
    find(word){
        var node = this.rootNode();

        for(var i=0; i<word.length; i++){
            var currentLetter = word[i];

            if(node.children[currentLetter]){
                node = node.children[currentLetter]
            } else{
                return false;
            }
        }
        return true
    }

    autoComplete(str){
        var node = this.rootNode();

        for(var i=0; i<word.length; i++){
            var currentLetter = word[i];

            if(node.children[currentLetter]){
                node = node.children[currentLetter]
            } else{
                return [];
            }
        }
        var queue = [];
        var word = [];
        if(node.completesString){
            word.push(node.val)
        }
        i=0
        for(var i=0; i<node.children.length; i++){
            queue.enqueue(Object.values(node.children)[i])
        }
        while(queue.length){
            node = queue.dequeue()
            for(var i=0; i<node.children.length; i++){
                queue.enqueue(Object.values(node.children)[i])
            }
            if(node.completesString){
                word.push(node.val)
            }
        }
        return word
    }
}   