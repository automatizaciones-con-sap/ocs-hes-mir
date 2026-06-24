import os
from src.adapters.sp_adapter import SharePointAdapter
from src.adapters.sap_adapter import SapAdapter
from src.services.sap_service import SapService
from src.services.order_list_service import OrderListService


def main():

    print("Starting OC Automation Process...")

    sp_adapter = SharePointAdapter()
    sap_service = SapService()
    list_service = OrderListService()

    df = sp_adapter.read_excel_file_from_sharepoint()

    if df is None or df.empty:
        print("Error: No exists sharepoint data or file is empty.")
        return

    order_list_obj = list_service.transformar_excel_a_modelos(df)
    ordenes = order_list_obj.get_order_list()

    print(f"Auditoría: {len(ordenes)} órdenes listas para procesamiento SAP.")

    if ordenes and sap_service.connect_sap():
        session = sap_service.get_session()
        sap_service.enter_to_transaction("ME21N")
        sap_adapter = SapAdapter(session)
        for i, oc in enumerate(ordenes, 1):
            try:
                nombre_prov = oc.get_provider().get_name()
                num_oc = oc.get_number()

                print(
                    f"🤖 [{i}/{len(ordenes)}] "
                    f"Cargando Proveedor: {nombre_prov}..."
                )

                sap_adapter.crear_orden_compra(oc)

                print(
                    f"✅ Éxito: Registro SAP completado para OC {num_oc}"
                )

            except Exception as e:
                print(
                    f"❌ Error crítico en OC "
                    f"{oc.get_number()}: {e}"
                )

    else:
        print("❌ Error de Conexión: SAP no disponible.")


if __name__ == "__main__":
    main()