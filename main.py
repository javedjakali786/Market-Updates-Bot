from functions import *

def main():

    grab_images()

    # send_image (channel_id, 'fear_greed.png')
    # send_image (channel_id, 'heat_map.png')

    send_image (chat_id, 'fear_greed.png')
    send_image (chat_id, 'heat_map.png')

    ''' Use #1 for channel messages and #2 for chat messages'''

if __name__ == '__main__':
    main()
