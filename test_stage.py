import sys

def test_1512(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change stage data-width
    content = content.replace('data-width="1440"', 'data-width="1512"')
    
    # Change nav box back to 1400px
    content = content.replace(
        'style="left:0; right:0; margin:0 auto; top:38px; width:1328px; height:66px; z-index:50;"',
        'style="left:0; right:0; margin:0 auto; top:38px; width:1400px; height:66px; z-index:50;"'
    )
    
    # Restore links left
    content = content.replace(
        'left:531px;',
        'left:560px;'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

test_1512('codegen.html')
print("Applied 1512px stage to codegen.html for testing.")
