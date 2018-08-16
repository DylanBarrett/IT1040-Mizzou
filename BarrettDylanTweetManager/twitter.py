import tweet
import pickle

def main():
    #tweetlist = []
    file_name = "tweets.dat"
    try:
        load_file = open(file_name,'rb')
        tweetlist = pickle.load(load_file)
        load_file.close()
    except:
        tweetlist = []

    while (True):
        ch = display_menu()
        if (ch==1):
            author = input("\nWhat is your name? ")
            text = input("What would you like to tweet? ")
            while (len(text) > 140):
                print("\nTweets can only be 140 characters!")
                text = input("\nWhat would you like to tweet? ")
            tweets = tweet.Tweet(author, text)
            tweetlist.append(tweets)
            try:
                outputfile = open(file_name, 'wb')
                pickle.dump(tweetlist, outputfile)
                outputfile.close()
                print(author, ", your tweet has been saved.\n",sep = "")
                
            except:
                print("Your tweets could not be saved!")
        elif(ch==2):
            tweetlist.reverse()
            
            #if(tweetlist == []):

                #load_file = open(file_name,'rb')
                #tweetlist = pickle.load(load_file)
                #load_file.close()
            print()
            print("Recent Tweets")
            print("-----------")
            if len(tweetlist) == 0:
                print("There are no recent tweets. \n")
            else:
                
                for tweets in tweetlist[:5]:
                    print(tweets.get_author(), "-", tweets.get_age())
                    print(tweets.get_text(),"\n")
            tweetlist.reverse()
                    
        elif(ch==3):
            match = 0
            tweetlist.reverse()
            if tweetlist == []:
                print()
                print("There are no tweets to search.\n")
                continue
            else:
                search = input("What would you like to search for? ")
                print ()
                print ("Search Results")
                print("----------")
                match = 0
                
                for tweets in tweetlist:  
                    if search in tweets.get_text():
                        matched_tweets = []
                        match = 1
                        matched_tweets.append(tweets) # append all the matches to an array
                        #for tweets in matched_tweets:
                        print(tweets.get_author(), "-", tweets.get_age())
                        print(tweets.get_text(), "\n")
                        
                if match == 0:
                    print("No tweets contained,", search)
                    print()
            
            tweetlist.reverse()
                
        elif(ch==4):
            print("Thank you for using the Tweet Manager!")
            print()
            #load_file = open(file_name, 'wb')
            #pickle.dump(tweetlist, load_file)
            #load_file.close()
            exit()
            
def display_menu():
    print("Tweet Menu")
    print("----------")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    print()
    while True:
            try:
                choice = int(input("What would you like to do? "))
                if choice < 1 or choice > 4:
                    print("Please select a valid option.\n")
                    
                    continue
                    
            except ValueError:
                print("Please enter a numeric value.\n")
            else:
                break
    return choice
            
main()
                



                
                
            
        
        
