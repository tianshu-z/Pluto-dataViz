import matplotlib.pyplot as plt
import math

# We use circular bar graph to visualize 3 emotion dimensions, i.e. valence, arousal, and dominance
# The value of emo-dimensions is transformed to radians (actually angles)

"""Inputs"""
# 3 dimensions is updated based on user's word-evaluating submission on TODAY page
# All 3 emotion dimension values are reset every midnight at 00:00.
valence = - 0.91
arousal = - 0.323
dominance = - 0.73
# Basic emotion is calculated based on the emotion dimensions
# Will be put in the middle of the diagram as a piece of text
basic_emo = 'Sadness'


"""Plotting"""
# We plot 3 values as circular (polarized) bars, essentially the same as columns.
ax = plt.subplot(projection = 'polar')  # custom projection
ax.barh(0, math.radians(0)) # these three center circular bars are used as placeholders, not super useful.
ax.barh(1, math.radians(0))
ax.barh(2, math.radians(0))

# Based on whether an emo-dimension value is larger or smaller than 0
# the bent bars have different colors and labels

# dominance 主导性
if dominance < 0:
    ax.barh(3, math.radians(180*dominance), color='#8E93E2') # set color
    label_3 = 'Submissive' # set label text 中文：被动
    label_align_3 = 'right' # set label alignment
elif dominance > 0:
    ax.barh(3, math.radians(180*dominance), color='#FFDC69')
    label_3 = 'Dominant' # 中文：主导
    label_align_3 = 'left'
else:
    label_3 = '~'
    label_align_3 = 'center'

# arousal 投入度
if arousal < 0:
    ax.barh(4, math.radians(180*arousal), color='#86E3C2')
    label_4 = 'Indifferent' #中文：疏离
    label_align_4 = 'right'
elif arousal > 0:
    ax.barh(4, math.radians(180 * arousal), color='#F5B6C4')
    label_4 = 'Excited' #中文：兴奋
    label_align_4 = 'left'
else:
    label_4 = '~'
    label_align_4 = 'center'

# Valence 快乐感
if valence < 0:
    ax.barh(5, math.radians(180*valence), color='#93D6DD')
    label_5 = 'Sad' #中文：低落
    label_align_5 = 'right'
elif valence > 0:
    ax.barh(5, math.radians(180*valence), color='#FDA17A')
    label_5 = 'Pleasant' #中文：快乐
    label_align_5 = 'left'
else:
    label_5 = '~'
    label_align_5 = 'center'


"""Fine-tuning"""

# Please note: we should refer to UI doc for more information on fine-tuning

ax.set_theta_zero_location('S')  # The direction of circular bar
#ax.set_theta_direction(-1) # clockwise or counterclockwise
ax.set_thetagrids([180,180,0], labels=[-1,1,0]) #label
ax.set_rgrids([6], labels=['']) # placeholder

# adding label as texts
plt.text(0, 5.2, label_5, fontsize=10, horizontalalignment=label_align_5)
plt.text(0, 4.2, label_4, fontsize=10, horizontalalignment=label_align_4)
plt.text(0, 3.2, label_3, fontsize=10, horizontalalignment=label_align_3)

# Today's Key Emotion information:
# 今日情绪关键词
# "恐惧"或其他
plt.text(0, -0.6, 'Key Emotion Today', color='#40C9E2', fontsize=12, fontweight='bold', horizontalalignment='center', verticalalignment='bottom')
plt.text(0, 0.5, basic_emo, fontsize=24, color='#A0A0A0',fontweight='bold', horizontalalignment='center')

plt.axis('off')  # remove all labels and axis, which we should refer to UI doc eventually
plt.show()