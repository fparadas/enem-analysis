import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

TABLE_NAME = "brasil-aberto-443222"
FULL_QUERY = f"""
WITH enem AS (
SELECT
    enem.`CO_MUNICIPIO_ESC`, 
    enem.`Q006`,
    enem.`Q001`,
    `NU_NOTA_CH`
    + `NU_NOTA_CN`
    + `NU_NOTA_LC`
    + `NU_NOTA_MT`
    + `NU_NOTA_REDACAO` AS nota_final,
FROM `brasil-aberto-443222.microdados_abertos.enem` AS enem
WHERE
    `NU_NOTA_CH`
    + `NU_NOTA_CN`
    + `NU_NOTA_LC`
    + `NU_NOTA_MT`
    + `NU_NOTA_REDACAO`
    > 0
AND enem.`IN_TREINEIRO` != 1
AND enem.`CO_MUNICIPIO_ESC` IS NOT NULL
)

SELECT
  enem.`Q001`,
  enem.`Q006`,
  enem.nota_final,
  ips.pop,
  ips.pib_pc,
  -- Nutrição e Cuidados Médicos Básicos
  ips.cv_polio,
  ips.hcsap,
  ips.macsap,
  ips.mi5,
  ips.subnutricao,
  -- Abastecimento e Esgotamento
  ips.aavrd,
  ips.esa,
  ips.iaa,
  ips.ipad,
  -- Moradia
  ips.dcra,
  ips.diea,
  ips.dpa,
  ips.dpsa,
  -- Segurança Pessoal
  ips.aj,
  ips.am,
  ips.homicidios,
  ips.mat,
  -- Acesso ao Conhecimento Básico
  ips.aef,
  ips.aem,
  ips.eem,
  ips.disem,
  ips.ideb_ef,
  ips.ref,
  -- Acesso à Informação e Comunicação
  ips.cim,
  ips.di_blf,
  ips.dtm,
  ips.qim,
  -- Saúde e Bem-estar
  ips.ev,
  ips.m15_50,
  ips.mdcnt,
  ips.obesidade,
  ips.suicidios,
  -- Qualidade do Meio Ambiente
  ips.avu,
  ips.eco2h,
  ips.fc,
  ips.ivcm,
  ips.svps,
  -- Direitos Individuais
  ips.apdh,
  ips.eadmn,
  ips.iadj,
  ips.tclp,
  -- Liberdades Individuais e de Escolha
  ips.acle,
  ips.ga19,
  ips.ppau,
  ips.ti,
  -- Inclusão Social
  ips.pgcm,
  ips.pnpcm,
  ips.vci,
  ips.vcn,
  ips.vcm,
  -- Acesso à Educação Superior
  ips.ees,
  ips.mees
FROM enem
INNER JOIN `brasil-aberto-443222.microdados_abertos.municipios_ips` AS ips
    ON (
        ips.codigo = CAST(enem.`CO_MUNICIPIO_ESC` AS STRING)
    )
"""

AGGREGATED_QUERY = """
WITH enem AS (
SELECT
    enem.`CO_MUNICIPIO_ESC`, enem.`Q006`,
    avg(`NU_NOTA_CH`
    + `NU_NOTA_CN`
    + `NU_NOTA_LC`
    + `NU_NOTA_MT`
    + `NU_NOTA_REDACAO`) AS nota_media,
FROM `brasil-aberto-443222.microdados_abertos.enem` AS enem
WHERE
    `NU_NOTA_CH`
    + `NU_NOTA_CN`
    + `NU_NOTA_LC`
    + `NU_NOTA_MT`
    + `NU_NOTA_REDACAO`
    > 0
AND enem.`IN_TREINEIRO` != 1
AND enem.`CO_MUNICIPIO_ESC` IS NOT NULL
GROUP BY enem.`CO_MUNICIPIO_ESC`, enem.`Q006`
)

SELECT
  enem.`Q006`,
  enem.nota_media,
  ips.pop,
  ips.pib_pc,
  ips.ips,
  ips.ncmb,
  ips.as,
  ips.moradia,
  ips.sp,
  ips.acb,
  ips.aic,
  ips.sb,
  ips.qma,
  ips.di,
  ips.lie,
  ips.inclusao,
  ips.aes
FROM enem
INNER JOIN `brasil-aberto-443222.microdados_abertos.municipios_ips` AS ips
    ON (
        ips.codigo = CAST(enem.`CO_MUNICIPIO_ESC` AS STRING)
    ) 
"""


def client(credentials: str) -> bigquery.Client:
    """
    Create a BigQuery client using the provided credentials.

    Args:
        credentials (str): Path to the service account key file.

    Returns:
        bigquery.Client: BigQuery client.
    """
    credentials = service_account.Credentials.from_service_account_file(
        "credentials.json"
    )

    return bigquery.Client("brasil-aberto-443222", credentials=credentials)

def fetch_data(client: bigquery.Client, query: str) -> pd.DataFrame:
    """
    Fetch data from BigQuery using the provided query.

    Args:
        query (str): SQL query to execute.

    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
    df = client.query(query).to_dataframe()

    return df

