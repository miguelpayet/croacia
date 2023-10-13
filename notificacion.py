import boto3
import properties


class Notificacion:

    def __init__(self):
        session = boto3.Session(profile_name='default')
        self.client = session.client('sns')

    def publicar(self, mensaje):
        response = self.client.publish(TopicArn=properties.get('topico'), Subject=properties.get('subject'),
                                       Message=mensaje, )
        print('mensaje enviado %s' % (response['MessageId']))
