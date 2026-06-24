from src.core.models.order_list import OrderList
from src.services.oc_service import OcService

class OrderListService:
    def __init__(self):
        self.oc_service = OcService()

    def transformar_excel_a_modelos(self, df) -> OrderList:
        ocs_container = OrderList([])

        for _, fila in df.iterrows():
            try:
                nueva_oc = self.oc_service.mapear_fila_a_objeto(fila)
                ocs_container.append_order(nueva_oc)
            except Exception as e:
                print(f"⚠️ Auditoría: Fila con OC {fila.get('OC')} rechazada en mapeo. Motivo: {e}")
        
        return ocs_container