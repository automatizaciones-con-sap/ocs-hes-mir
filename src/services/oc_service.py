from src.core.models.order import Order
from src.core.models.provider import Provider
from src.core.models.customer import Customer
from src.core.models.organization import Organization
from src.core.models.service import Service
from src.core.models.transaction import Transaction

class OcService:
    def mapear_fila_a_objeto(self, fila) -> Order:

        org = Organization(
            purchase_organization_code=fila['PA_ORG_COMPRAS'], #U03 U0O2
            purchase_organization=fila['PA_GRUPO_COMPRAS'],
            society_code=fila['PA_SOCIEDAD']
        )
        
        srv = Service(
            i=fila['PA_I'],
            p=fila['PA_P'],
            name=fila['DESCRIPCIÓN'],
            article_group=fila['GRUPO_ARTICULO'], 
            num_service=fila['SERVICIO'],
            quantity=1,
            gross_price=fila['IMPORTE_SIN_IGV']
        )

        prov = Provider(
            name= '',
            identifier=fila['ID_EMPRESA'],
            cost_center=fila['PA_CENTRO_COSTO']
        )
        
        cust = Customer(
            sap_code=fila['CÓDIGO'],
            name=fila['ESTACIÓN'],
            applicant_code=fila['PA_SOLICITANTE']
        )

        trx = Transaction( code="me21n" )

        return Order(
            type=fila['PA_TIPO_ORDEN'],
            number='',
            date=fila['FECHA_FC'],
            state='',
            customer=cust,
            organization=org,
            provider=prov,
            service=srv,
            transaction=trx
        )