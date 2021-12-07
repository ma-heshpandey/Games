from words import words
from life_of_hangman import dict_for_hang_man
import random
display_space=[]


def computer_choice():
    word_chosen=list(random.choice(words).lower())
    #word_chosen='mahesh'
    return word_chosen

def user_choice_of_words():
    computer_word=computer_choice()
    user_word=input('Enter the guess word\n',).lower()   
    while not user_word.isalpha():
        user_word=input('Enter the guess word\n').lower()    

    return user_word


def game_play():
    
    computer_word_chosen=computer_choice()
    dict_for_words={}
    dictionary_for_index={}
    typed_word_by_user=[]
    for i in computer_word_chosen:display_space.append('_ ') #insert _ for words by computer
    
    #for counting no of instances of alphabets in number making each alphabet a key of dictionary
    for alphabets in computer_word_chosen:
            dict_for_words.setdefault(alphabets,0)
            dict_for_words[alphabets]=dict_for_words[alphabets]+1
    
    lives=7
    index=0 #for knowing index of each word in computer word
    
    dict_for_words_updated_words=dict_for_words.copy() #for decreasing instances number
    
    #for making dictionary for word as key and value index of words
    for alphabets in computer_word_chosen:      
            if alphabets not in dictionary_for_index:
                dictionary_for_index.setdefault(alphabets,[computer_word_chosen.index(alphabets)])
            else:dictionary_for_index[alphabets]=dictionary_for_index[alphabets]+[index]
            index=index+1
    
    

    while lives!=0:
        print('\nGuess the word=>'+''.join(display_space))
        user_word=user_choice_of_words()
        i=len(computer_word_chosen)

        
        if (user_word not in computer_word_chosen):
            typed_word_by_user.append(user_word+' ')

        if ((user_word+' ') in display_space): #to check for repeating alphabets by user so can be updated in wrong alphabets by user
            total_no_of_word=dict_for_words[user_word]
            total_instances_by_user=0

            for word in display_space:
                if user_word+' '== word:
                  total_instances_by_user=total_instances_by_user+1 
                  

            updated_total_instances_by_user=total_instances_by_user+1    
            print(updated_total_instances_by_user)  
            if updated_total_instances_by_user>total_no_of_word:
                    typed_word_by_user.append(user_word+' ')


            

        if user_word in computer_word_chosen:
            

            if dict_for_words_updated_words[user_word]==0:
                lives=lives-1
                temp=(''.join(computer_word_chosen)) #to convert list to string
                if lives==0:print(f'Sorry you lost your life.\nThe word was=> {temp}') 

            #for updating display spaces with spaces and correct user enter alphabets
            if dict_for_words_updated_words[user_word]!=0: 
                dict_for_words_updated_words[user_word]=dict_for_words_updated_words[user_word]-1
                if dict_for_words[user_word]==1: 
                    display_space[dictionary_for_index[user_word][0]]=user_word+' '
                    
                else: 
                    display_space[dictionary_for_index[user_word][dict_for_words_updated_words[user_word]]]=user_word+' '
                    greater_by=dict_for_words[user_word]-dict_for_words_updated_words[user_word]

        
        else:
            lives=lives-1
            temp=(''.join(computer_word_chosen))
            if lives==0:print(f'Sorry, you lost your life.\nThe word was => {temp}') 

        
        #if display_space==' '.join(list(computer_word_chosen)):print('Hurray! You won\n\n')    
        
        #for checking complition of word
        check_variable=''.join(display_space)
        if check_variable.replace(' ','')== computer_word_chosen:
            print('Hurray!You won\n\n')
            break
        print('The incorrect words typed are =>',''.join(typed_word_by_user)+'\n')

        print(dict_for_hang_man[lives])

if __name__=="__main__":
    game_play()



