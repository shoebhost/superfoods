from PIL import Image
import streamlit as st
# making a landing page!
st.set_page_config(page_title="Super Foods", layout="wide")

img_foods = Image.open("images/long_lasting_bread.png") 
img_food  = Image.open("images/marinara.jpg")
new_image = img_foods.resize ((310,170))
image = img_food.resize ((340,270)) 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')

with st.container():
  st.subheader("The Army’s Forgotten Food Miracle!")
  st.title('The Ultimate Survival Super Foods.')
  st.write('''With over 126 forgotten survival foods and storage hacks ["The Lost Superfoods"]( https://www.digistore24.com/redir/377301/digitalmarkie/) is a vital book to have in your survival stockpile. There are many essential foods that are often overlooked in traditional survival stores, such as wild edible plants, nuts, seeds, mushrooms, and even insects. This book provides detailed information on how to identify and prepare all of these foods, as well as insight into their nutritional value and storage techniques. You'll discover one of the foods that kept a few people well fed during the Leningrad siege, while famine gripped the city around them.''')
c = st.container()
with st.container():
    c.write('###')
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image (image, caption = 'Delicious dehydrated marinara sauce')
    with text_column:
        ('''The nutrients found in this food are rich in butyric acid and will also help you absorb the maximum amount of nutrition from any other food you may consume as a result of protecting your gut lining. [Butyric acid]( https://www.digistore24.com/redir/377301/digitalmarkie/) also helps to reduce inflammation in the gut, which can help with digestive issues, such as bloating and constipation. It also helps to improve the balance of the gut microbiome, promoting healthy digestion and absorption of nutrients. Butyric acid helps to promote regular and healthy bowel movements, while also providing other benefits such as supporting the immune system and reducing the risk of heart disease. This will help you stretch your food stockpile.''')

        st.write('''You'll also discover the recipe for the survival food that saved the [Europeans during the Dark Ages,]( https://www.digistore24.com/redir/377301/digitalmarkie/)  and especially as the Black Plague was ravaging the countryside. I'm also planning to teach you how to make Mountaineer's Tuna Stroganoff, which is one of the most satisfying survival foods ever invented. A long time ago I decided to build my stockpile around as many tasty foods as possible without sacrificing shelf life.''')

with st.container():
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image (new_image, caption = 'Long-lasting bread developed by the Cree Tribe of Canada')
    with text_column:
        st.write(
            '''Unopened canned tuna lasts for years, with the tuna retaining best quality for 3 to 5 years. You'll also find out how to feed yourself for a whole month using just 100USD at Walmart the wild-growing superfoods that almost nobody knows about, the ins and outs of canning both vegetables and meat safely for 20 years, how to prevent your foods from going rancid, seven deadly canning mistakes to avoid like the plague, how to make yourself a $20 DIY Food Bucket better than anything on the market today and the best 50 foods to dehydrate for your food stockpile. With this knowledge, you can create a [long-lasting food source]( https://www.digistore24.com/redir/377301/digitalmarkie/) for yourself and your family, ensuring that your pantry remains full for years to come.''')
    st.subheader('[Grab Your Copy!](https://www.digistore24.com/redir/377301/digitalmarkie/)')
with st.container():
  st.write("---")  
  st.header("Subscribe")
  st.write("##")
  contact_form = """
  <form action="https://formsubmit.co/311724b541bce2c5ee47a45341602a85" method="POST">
     <input type="hidden" name="_captcha" value='false'>
     <input type="text" name="name" placeholder="Your Name"required>
     <input type="email" name="email" placeholder="Your Email Address" required>
     <button type="submit">Send</button>
  </form>
  """
  left_column, right_column = st.columns(2)
  with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
