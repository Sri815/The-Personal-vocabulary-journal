import kivy
kivy.require('1.10.0')

#from kivy.uix.stacklayout import StackLayout
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.app import App
#from kivy.uix.popup import Popup  
from kivy.uix.screenmanager import ScreenManager, Screen 
#from kivy.lang import Builder 
from kivy.properties import ObjectProperty
#from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget

import json

class MenuPage(Screen):
	pass

class DisplayPage(Screen):
	search_box= ObjectProperty()
	label_maening=StringProperty()
	label_synonym=StringProperty()
	label_ant=StringProperty()
	label_sentence=StringProperty()
	

	#def __init__(self, **kwargs):
	#	super(DisplayPage,self).__init__(**kwargs)
		

	def search_function(self):
		with open('vocab_words.json') as rfile:
			data=json.load(rfile)

		word=self.search_box.text 

		for value in data:
			if value['word']==word:
				self.label_maening=value['meaning']
				self.label_synonym=value['synonym']
				self.label_ant=value['antonyms']
				self.label_sentence=value['sentence']


class NewWordPage(Screen):
	word_box = ObjectProperty()
	meaning_box = ObjectProperty()
	synonym_box = ObjectProperty()
	ant_box = ObjectProperty()
	sentence_box = ObjectProperty()
	

	def saving_data(self):
		
		with open('vocab_words.json') as rfile:
			data=json.load(rfile)
			

		entry={'word': self.word_box.text, 'meaning': self.meaning_box.text, 'synonym': self.synonym_box.text, 'antonyms': self.ant_box.text, 'sentence': self.sentence_box.text}
		data.append(entry)
		
			
		with open('vocab_words.json','w') as wfile:
			json.dump(data,wfile,indent=4)

		card=['flash_card1.json','flash_card2.json','flash_card3.json','flash_card4.json','flash_card5.json','flash_card6.json','flash_card7.json','flash_card8.json','flash_card9.json','flash_card10.json']

		for i in card:
			with open(i) as frfile:
				flash_data=json.load(frfile)

			if len(flash_data)<40:
				flash_data.append(entry)

				with open(i,'w') as frfile:
					json.dump(flash_data,frfile,indent=4)

				break
			else:
				continue

class FlashCard(Screen):
	def on_press(self,index):
		flash_display_screen = self.manager.get_screen('flash_display')
		setattr(flash_display_screen, 'index', index)
		self.manager.current='flash_display'
	
class FlashDisplayPage(Screen):
	
	def on_enter(self):
		Num=self.index
		card=['flash_card1.json','flash_card2.json','flash_card3.json','flash_card4.json','flash_card5.json','flash_card6.json','flash_card7.json','flash_card8.json','flash_card9.json','flash_card10.json']
		
		with open(card[Num+1]) as frfile:
			flash_data=json.load(frfile)

		for i in flash_data:
			d=str(i['word']+' : \n   '+i['meaning'])
			label=Label(text=d)
			self.ids.pages.add_widget(label)


class WordGroups(Screen):
	pass

class Manager(ScreenManager):
	pass

class VocabularyJournalApp(App):
	def build(self):
		return Manager()

obj = VocabularyJournalApp()
obj.run()
