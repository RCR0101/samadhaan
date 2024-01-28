from common_func import clean_text
from transformers import  pipeline
import torch
# from sentiment_text import get_sentiment

def rephrase_text(text, language='en'):
   
    rephraser = init_rephrase_model()
    response = rephraser(text, max_length=100, num_beams=5, early_stopping=True)
    return response[0]['generated_text']

def init_rephrase_model():
    rephraser = pipeline('text-generation', model='t5-base')
    return rephraser

def summarize_text(text, max_length=140):
    # Load the pre-trained summarization model
    summarizer = init_summarize_model()

    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)

    # Return the summary as a string
    return summary[0]['summary_text']

def init_summarize_model():
    summarizer = pipeline("summarization", model='t5-base')
    return summarizer

# new_complaint_text  =  "Telecommunications >> Mobile Related >> Tariff / Recharge issue / Billing issue of Postpaid\r\n\r\nMobile Number : X4X1X1X4X1\r\nService Provider : Bharat Sanchar Nigam Limited Corporate Office\r\n-----------------------\r\nRespected sir ,\r\nI tried to recharge my BSNL number on 27 jan23, money was deducted, yet I have not received recharge benefits. Details are as follows-\r\nMobile Number - X4X1X1X4X1\r\nOperator Reference Id -X0X0X1X7X4X4X5\r\nAmount-153/-\r\nPls look into the matter and resolve the issue as soon as possible so I can enjoy hassle-free service.\r\n\r\nRegards.\r\nAnshu karn"
# new_complaint_text_cleaned = clean_text(new_complaint_text)
# sentiment = get_sentiment(new_complaint_text_cleaned)
# new_rephrase = rephrase_text(new_complaint_text_cleaned)
# sum_ms = summarize_text(new_complaint_text_cleaned)

# print("\nNew Summary:", sum_ms)
# print("\nRephrased Text :", new_rephrase)
# print(f"\nSentiment: {sentiment['label']}, Confidence: {sentiment['score']:.2f}")