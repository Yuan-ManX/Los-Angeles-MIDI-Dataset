# -*- coding: utf-8 -*-
"""Los_Angeles_MIDI_Dataset_Search_and_Explore.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zICuSnqe_EpScHcfG6LS4-04adDHTUPD

# Los Angeles MIDI Dataset: Search and Explore (ver. 0.8)

***

Powered by tegridy-tools: https://github.com/asigalov61/tegridy-tools

***

#### Project Los Angeles

#### Tegridy Code 2022

***

# (Setup Environment)
"""

#@title Install all dependencies (run only once per session)

!git clone https://github.com/asigalov61/Los-Angeles-MIDI-Dataset
!pip install matplotlib
!pip install sklearn
!pip install pickle5
!pip install tqdm

#@title Import all needed modules

print('Loading needed modules. Please wait...')
import os
import copy
import pickle5
from tqdm import tqdm

print('Loading MIDI.py module...')
os.chdir('/content/Los-Angeles-MIDI-Dataset')
import MIDI

from sklearn.metrics import pairwise_distances, pairwise
import matplotlib.pyplot as plt

os.chdir('/content/')
print('Done!')

# Commented out IPython magic to ensure Python compatibility.
#@title Unzip LAMDa data
# %cd /content/Los-Angeles-MIDI-Dataset/META-DATA

print('=' * 70)
print('Unzipping META-DATA...Please wait...')

!cat LAMDa_META_DATA.zip* > LAMDa_META_DATA.zip
print('=' * 70)

!unzip -j LAMDa_META_DATA.zip
print('=' * 70)

print('Done! Enjoy! :)')
print('=' * 70)
# %cd /content/

#================================================

# %cd /content/Los-Angeles-MIDI-Dataset/MIDI-MATRIXES

print('=' * 70)
print('Unzipping MIDI-MATRIXES...Please wait...')

!cat LAMDa_MIDI_MATRIXES.zip* > LAMDa_MIDI_MATRIXES.zip
print('=' * 70)

!unzip -j LAMDa_MIDI_MATRIXES.zip
print('=' * 70)

print('Done! Enjoy! :)')
print('=' * 70)
# %cd /content/

#==================================================

# %cd /content/Los-Angeles-MIDI-Dataset/TOTALS

print('=' * 70)
print('Unzipping TOTALS...Please wait...')

!unzip -j LAMDa_TOTALS.zip
print('=' * 70)

print('Done! Enjoy! :)')
print('=' * 70)
# %cd /content/

#@title Load LAMDa data
print('==' * 70)
print('Loading LAMDa data...Please wait...')
print('==' * 70)
print('Loading LAMDa META-DATA...')
meta_data = pickle5.load(open('/content/Los-Angeles-MIDI-Dataset/META-DATA/LAMDa_META_DATA.pickle', 'rb'))
print('Done!')
print('==' * 70)
print('Loading LAMDa MIDI-MATRIXES...')
midi_matrixes = pickle5.load(open('/content/Los-Angeles-MIDI-Dataset/MIDI-MATRIXES/LAMDa_MIDI_MATRIXES.pickle', 'rb'))
print('Done!')
print('==' * 70)
print('Loading LAMDa TOTALS...')
totals = pickle5.load(open('/content/Los-Angeles-MIDI-Dataset/TOTALS/LAMDa_TOTALS.pickle', 'rb'))
print('Done!')
print('==' * 70)
print('Enjoy!')
print('==' * 70)

#@title Load helper functions
#=================================================================================

def compress_matrix(midi_matrix):

  MX = 38
  MY = 256

  if len(midi_matrix) == MX:

    compressed_matrix = []
    zeros = 0
    zeros_shift = 0
    zeros_count = 0

    for m in midi_matrix:
      for mm in m:
        zeros_shift = max(zeros_shift, mm) + 1

    compressed_matrix.append(zeros_shift)

    for m in midi_matrix:
      if len(m) == MY:
        for mm in m:
          if mm != 0:
            if zeros > 0:
              compressed_matrix.append(zeros+zeros_shift)
              zeros = 0
            compressed_matrix.append(mm)
          
          else:
            zeros += 1
            zeros_count += 1
      
      else:
        print('Wrong matrix format!')
        return [1]

    if zeros > 0:
      compressed_matrix.append(zeros+zeros_shift)

    compressed_matrix.append(zeros_count+zeros_shift)
    compressed_matrix.append(zeros_shift)

    return compressed_matrix

  else:
    print('Wrong matrix format!')
    return [0]

#=================================================================================

def decompress_matrix(compressed_midi_matrix):

  MX = 38
  MY = 256

  zeros_count = 0

  temp_matrix = []
  decompressed_matrix = [[0]*MY for i in range(MX)]

  if compressed_midi_matrix[0] == compressed_midi_matrix[-1]:
    zeros_shift = compressed_midi_matrix[0]
    mcount = 0

    for c in compressed_midi_matrix[1:-2]:
      if c > zeros_shift:
        temp_matrix.extend([0] * (c-zeros_shift))
        zeros_count += (c-zeros_shift)

      else:
        temp_matrix.extend([c])

    if len(temp_matrix) == (MX * MY):

      for i in range(MX):
        for j in range(MY):
          decompressed_matrix[i][j] = copy.deepcopy(temp_matrix[(i*MY) + j])
      
      if len(decompressed_matrix) == MX and zeros_count == (compressed_midi_matrix[-2]-zeros_shift):
        return decompressed_matrix

      else:
        print('Matrix is corrupted!')
        return [len(decompressed_matrix), (MX * MY), zeros_count, (compressed_midi_matrix[-2]-zeros_shift)]
    
    else:
      print('Matrix is corrupted!')
      return [len(temp_matrix), zeros_count]

  else:
    print('Matrix is corrupted!')
    return [0]

#=================================================================================

"""# (TOTALS)"""

#@title Plot Totals
cos_sim = pairwise.cosine_similarity(
      totals[0][0][4] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()
# plt.close()

cos_sim = pairwise.cosine_similarity(
      totals[0][0][5] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()


cos_sim = pairwise.cosine_similarity(
      totals[0][0][6] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()

cos_sim = pairwise.cosine_similarity(
      totals[0][0][7] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()

cos_sim = pairwise.cosine_similarity(
      totals[0][0][8] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()

cos_sim = pairwise.cosine_similarity(
      totals[0][0][9] 
  )
plt.figure(figsize=(8, 8))
plt.imshow(cos_sim, cmap="inferno", interpolation="none")
im_ratio = 1
plt.colorbar(fraction=0.046 * im_ratio, pad=0.04)
plt.xlabel("Position")
plt.ylabel("Position")
plt.tight_layout()
plt.plot()

"""# (SEARCH)"""

#@title MIDI Matrixes Search
full_path_to_MIDI_file = "/content/Los-Angeles-MIDI-Dataset/Come-To-My-Window-Modified-Sample-MIDI.mid" #@param {type:"string"}
matching_type = "minkowski" #@param {type:"string"}
print('=' * 70)
print('Loading MIDI file...')

score = MIDI.midi2ms_score(open(full_path_to_MIDI_file, 'rb').read())

events_matrix = []

itrack = 1

while itrack < len(score):
    for event in score[itrack]:         
      events_matrix.append(event)
    itrack += 1

# Sorting...
events_matrix.sort(key=lambda x: x[1])

# recalculating timings
for e in events_matrix:
    e[1] = int(e[1] / 10)
    if e[0] == 'note':
      e[2] = int(e[2] / 20)

# final processing...

melody_chords = []

patches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pe = events_matrix[0]
for e in events_matrix:

  if e[0] == 'note':
    # ['note', start_time, duration, channel, note, velocity]
    time = max(0, min(255, e[1]-pe[1]))
    duration = max(1, min(255, e[2]))
    channel = max(0, min(15, e[3]))

    if e[3] != 9:
      instrument = max(0, min(127, patches[e[3]]))
    else:
      instrument = max(128, min(255, patches[e[3]]+128))

    if e[3] != 9:

      pitch = max(1, min(127, e[4]))
    else:
      pitch = max(129, min(255, e[4]+128))

    if e[3] != 9:
      velocity = max(1, min(127, e[5]))
    else:
      velocity = max(129, min(255, e[5]+128))

    melody_chords.append([time, duration, channel, instrument, pitch, velocity])

  if e[0] == 'patch_change':
    # ['patch_change', dtime, channel, patch]
    time = max(0, min(127, e[1]-pe[1]))
    channel = max(0, min(15, e[2]))
    patch = max(0, min(127, e[3]))

    patches[channel] = patch

  pe = e # Previous event

MATRIX = [[0]*256 for i in range(38)]

for m in melody_chords:

  MATRIX[0][m[0]] += 1
  MATRIX[1][m[1]] += 1
  MATRIX[2][m[2]] += 1 
  MATRIX[3][m[3]] += 1
  MATRIX[4][m[4]] += 1
  MATRIX[5][m[5]] += 1
  MATRIX[m[2]+6][m[3]] += 1
  MATRIX[m[2]+22][m[4]] += 1

print('Dones!')
print('=' * 70)

print('Searching...Please wait...')

scores = []

for D in tqdm(midi_matrixes):
    dist = pairwise_distances(MATRIX, 
                             decompress_matrix(D[1]),
                              metric=matching_type)[0][0]
                              
    scores.append(dist)
    if dist == 0:
      print('Found exact match!')
      print('Stoping further search...')
      break

print('Done!')
print('=' * 70)
    
print('Euclidian distance ==', min(scores))
print('=' * 70)
print('LAMDa File Name:', midi_matrixes[scores.index(min(scores))][0])
print('=' * 70)

#@title Meta-Data Search
search_query = "Come To My Window" #@param {type:"string"}

fields_to_search = ['track_name', 'text_event', 'lyric']

for d in tqdm(meta_data):
  for dd in d[1]:
    if dd[0] in fields_to_search:
      if str(search_query) in str(dd[2]):
        print(meta_data.index(d), dd[2])

"""# Congrats! You did it! :)"""