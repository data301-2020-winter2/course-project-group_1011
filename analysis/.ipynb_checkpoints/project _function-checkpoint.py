{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "numerical-messaging",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "def read_and_process(path):\n",
    "    df = (\n",
    "        pd.read_csv(path)\n",
    "        .rename(columns={\"track\":\"Track\", \"artist\":\"Artist\", \"danceability\":\"Danceability\", \"energy\":\"Energy\", \"key\":\"Key\", \"loudness\":\"Loudness\", \"mode\":\"Mode\", \"speechiness\":\"Speechiness\", \"acousticness\":\"Acousticness\", \"instrumentalness\":\"Instrumentalness\", \"liveness\":\"Liveness\", \"valence\":\"Valence\", \"tempo\":\"Tempo\", \"time_signature\":\"Time Signature\", \"target\":\"Target\"})\n",
    "        .drop(axis =1, columns={'chorus_hit','sections','duration_ms','speechiness','acousticness','instrumentalness','uri','liveness'})\n",
    "        .dropna()\n",
    "    )\n",
    "    \n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
