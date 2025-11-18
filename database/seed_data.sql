-- Datos semilla para instrumentos_financieros
-- SIESIF - Sistema Experto de Inversión Financiera
-- Basado en el Catálogo de Instrumentos Financieros (Tabla 2 - Avance 2)

-- Limpiar tabla si existe
TRUNCATE TABLE instrumentos_financieros RESTART IDENTITY CASCADE;

-- Insertar los 11 instrumentos financieros del catálogo oficial

-- 1. CETES
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'CETES',
    'renta_fija',
    'bajo',
    'Certificados de la Tesorería de la Federación. Bonos de corto plazo emitidos por el Gobierno Federal; no pagan cupones, se compran con descuento y al vencimiento devuelven el valor nominal.',
    '10-11% anual',
    'corto',
    'alta',
    CURRENT_TIMESTAMP
);

-- 2. Bonos M
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Bonos M',
    'renta_fija',
    'bajo_medio',
    'Deuda soberana a tasa fija con cupones semestrales y plazos de 3 a 30 años. Sensibles a cambios en tasas de interés, adecuados para objetivos de mediano y largo plazo.',
    '8-10% anual',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 3. Udibonos
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Udibonos',
    'renta_fija',
    'bajo',
    'Bonos vinculados a la inflación que pagan una tasa real más la variación de la UDI. Ayudan a preservar el poder adquisitivo en el mediano y largo plazo.',
    '4-6% real + inflación',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 4. Bondes F
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Bondes F',
    'renta_fija',
    'bajo',
    'Bonos de tasa flotante cuyo cupón se ajusta periódicamente con una tasa de referencia de corto plazo. Minimizan la exposición a cambios de tasas a largo plazo.',
    '9-11% anual',
    'mediano',
    'alta',
    CURRENT_TIMESTAMP
);

-- 5. Bonos del IPAB
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Bonos del IPAB',
    'renta_fija',
    'bajo',
    'Títulos emitidos por el IPAB (BPAG y BPA) referenciados a CETES o tasa de fondeo. Algunos protegen contra la inflación. Bajo riesgo por respaldo público.',
    '8-10% anual',
    'mediano',
    'media_alta',
    CURRENT_TIMESTAMP
);

-- 6. Acciones
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Acciones',
    'renta_variable',
    'alto',
    'Participación en empresas listadas en BMV o BIVA. Alto potencial a largo plazo con volatilidad en el corto. Algunas pagan dividendos. Requieren diversificación.',
    '10-20% anual (variable)',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 7. ETFs
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'ETFs',
    'mixto',
    'medio',
    'Fondos cotizados que replican un índice y se operan como acciones. Ofrecen diversificación inmediata y bajas comisiones. El riesgo depende del índice que replican.',
    '8-15% anual',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 8. Fondos de Inversión (Deuda)
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Fondos de Inversión (Deuda)',
    'renta_fija',
    'bajo_medio',
    'Vehículos administrados por profesionales que agrupan recursos en carteras de deuda. Se valoran y ofrecen liquidez diaria.',
    '7-10% anual',
    'mediano',
    'alta',
    CURRENT_TIMESTAMP
);

-- 9. Fondos de Inversión (Mixtos)
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Fondos de Inversión (Mixtos)',
    'mixto',
    'medio',
    'Fondos que combinan instrumentos de renta fija y renta variable. Balance entre seguridad y rendimiento. Administrados profesionalmente.',
    '10-15% anual',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 10. Fondos de Inversión (Renta Variable)
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'Fondos de Inversión (Renta Variable)',
    'renta_variable',
    'alto',
    'Fondos que invierten principalmente en acciones. Mayor potencial de rendimiento con mayor volatilidad. Requieren horizonte de inversión largo.',
    '12-20% anual (variable)',
    'largo',
    'alta',
    CURRENT_TIMESTAMP
);

-- 11. FIBRAS
INSERT INTO instrumentos_financieros (nombre, tipo, riesgo, descripcion, rendimiento_referencial, horizonte_recomendado, liquidez, fecha_actualizacion)
VALUES (
    'FIBRAS',
    'alternativo',
    'medio',
    'Fideicomisos que invierten en bienes raíces, infraestructura o energía. Pagan distribuciones periódicas de rentas o flujos. Cotizan en bolsa.',
    '8-12% anual',
    'largo',
    'media',
    CURRENT_TIMESTAMP
);