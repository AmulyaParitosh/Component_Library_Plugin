import certifi
from PySide6.QtNetwork import (QNetworkAccessManager, QNetworkReply,
                               QNetworkRequest, QSsl, QSslCertificate,
                               QSslConfiguration, QSslSocket)

sslConfig = QSslConfiguration.defaultConfiguration()
sslConfig.setProtocol(QSsl.SslProtocol.TlsV1_0)
sslConfig.setPeerVerifyDepth(1)
sslConfig.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyPeer)
qcerts = QSslCertificate.fromPath(
	certifi.where(),
	QSsl.EncodingFormat.Pem,
	QSslCertificate.PatternSyntax.Wildcard,
)

sslConfig.setCaCertificates(qcerts)


def handleResponse(reply: QNetworkReply):

    er = reply.error()

    if er == QNetworkReply.NetworkError.NoError:
        print(reply.url().toString(), ":", reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute))

    elif er == QNetworkReply.NetworkError.ProtocolUnknownError:
        print("Blank URL passed!")

    else:
        print("Error occured: ", er)
        print(reply.url().toString(), reply.errorString())


network_access_manager = QNetworkAccessManager()
network_access_manager.finished.connect(handleResponse)
