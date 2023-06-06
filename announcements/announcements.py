import domControl
import crud_announcement
# builds an announcement and adds it to the html
def build_announcement(list, index):

  # read from the list at index
  announcement_content = f'''
  <div class = 'announcement'>
    <h4>
      {list[index]["_title"]}
    </h4>
    
    <p>
      {list[index]["_text"]}
    </p>
  </div>
  '''
  
  return announcement_content
  

# get announcement list from announcement crud
announcement_list = crud_announcement.get_existing_data("announcement.json")

# amount of announcements based on lenght of list
num_of_announcements = len(announcement_list)

announcement_box_content = "<div class = 'announcement-box'>"

# loop and make an announcement for each
for i in range(num_of_announcements):
  announcement_box_content += build_announcement(announcement_list, i)


announcement_box_content += '</div>'

# build announcement box
domControl.attach_content_to_element('pyscript-announcements', domControl.build_element(
  type='div',
  class_name='announcement-box',
  id='announcement', 
  content=announcement_box_content,))
  