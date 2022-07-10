from keyphrase_vectorizers import KeyphraseCountVectorizer


def get_full_aws_vocab():
    import pandas as pd
    df = pd.read_csv('vocabulary.csv', )
    service_name_list = [service_name.replace("Amazon", "") for service_name in df.ServiceName.to_list()]
    service_short_name_list = df.ServiceShortName.to_list()
    service_short_name_list.extend(service_name_list)
    return service_short_name_list


full_vocob_list = get_full_aws_vocab()
vectorizer = KeyphraseCountVectorizer()
