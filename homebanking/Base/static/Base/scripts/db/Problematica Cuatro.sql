--- 1) Listar la cantidad de clientes por nombre de sucursal ordenando de mayor a menor

--- 2) Obtener la cantidad de empleados por cliente por sucursal en un número real

--- 3) Obtener la cantidad de tarjetas de crédito por tipo por sucursal

--- 4) Obtener el promedio de créditos otorgado por sucursal

--- 5) La información de las cuentas resulta critica para la compañía, por eso es necesario crear una tabla denominada “auditoria_cuenta” para guardar los datos movimientos,
--- con los siguientes campos: old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at
--- Crear un trigger que después de actualizar en la tabla cuentas los campos balance, IBAN o tipo de cuenta registre en la tabla auditoria
--- Restar $100 a las cuentas 10,11,12,13,14 */

--- 6)Mediante índices mejorar la performance la búsqueda de clientes por DNI */

--- 7)Crear la tabla “movimientos” con los campos de identificación del movimiento, número de cuenta, monto, tipo de operación y hora
--- Mediante el uso de transacciones, hacer una transferencia de 1000$ desde la cuenta 200 a la cuenta 400
--- Registrar el movimiento en la tabla movimientos
--- En caso de no poder realizar la operación de forma completa, realizar un ROLLBACK */