class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        banned_set=set(banned)
        word_count={}
        result=""
        count =0
        words = ''.join(char if char.isalnum() else ' ' for char in paragraph).split()
        for word in words:
            if word not in banned_set:
                if word in word_count:
                    word_count[word]+=1
                else:
                    word_count[word]=1

                if word_count[word]>count:
                    count=word_count[word]
                    result=word

        return result
                

