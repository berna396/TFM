from datetime import datetime
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = MIMEMultipart("alternative")
    message["Subject"] = "Alerta Desconocida"
    message["From"] = 'testalertingtfm@outlook.es'
    message["To"] = 'testalertingtfm@outlook.es'

    # Create the plain-text and HTML version of your message
    text = """\
    Alerta Desconocida,
    Reporte:
    """
    html = """\
    
<!DOCTYPE html>
<html class='layout-pf'>
  <head>
    <title>Logreduce of /home/adrian/Desktop/TFM/Modelo/LOG_ERROR/log_fail1.log</title>
    <meta charset='UTF-8'>
    <link rel='stylesheet' type='text/css' href='https://cdnjs.cloudflare.com/ajax/libs/patternfly/3.24.0/css/patternfly.min.css'>
    <link rel='stylesheet' type='text/css' href='https://cdnjs.cloudflare.com/ajax/libs/patternfly/3.24.0/css/patternfly-additions.min.css'>
    <style>
.loglines {max-height: 800px; overflow-y: scroll;}
.list-group-item-container {overflow: hidden;}
.ls {margin-top: 0px; margin-bottom: 10px; border-color: black;}
#debuginfo {display: none;}
    </style>
  </head>
  <body>
    <nav class="navbar navbar-default navbar-pf" role="navigation">
      <div class="navbar-header">
        <img src="data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXBAMAAAASBMmTAAAAFVBMVEU6feU9geVjl+WMsOUicOXAz+X///9aF/8vAAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfiCAsFFSh04lDsAAAAp0lEQVQY012QXQ7CQAiE158LyKYH6BDf7WAPYEkP4BLvfxVxWxPjhge+sAwDpfy9oxgfX5hQhbctt0VV4Z1OjTVC+OowtqeNrekH7rO7qq/3/HcAZoIzOZZy5uDtIrHKlEN0Yg9D9kugQkVbTaDxMkAM9lOJuvWAhinwkR782dVS+iAwjpqzsDlYr7uDcsKPt3TtEc7o+8Siqeb7doQI9jwFjcv/YcobPpYhOB4CZRcAAAAASUVORK5CYII=" alt="LogReduce" />
      </div>
      <div class="collapse navbar-collapse navbar-collapse-1">
        <ul class="nav navbar-nav navbar-utility">
          <li><a href="#" id='debugbtn'>Show Debug</a></li>
          <li><a href="https://pypi.org/project/logreduce/" target="_blank">
            Documentation
          </a></li>
          <li><a href="#"><strong>Version</strong> 0.6.1</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-primary">
            <li class="active"><a href="log-classify.html">Report</a></li>
            <li><a href="ara-report/">ARA Records Ansible</a></li>
            <li><a href="./">Job Artifacts</a></li>
        </ul>
      </div>
    </nav>
    <div class="container" style='width: 100%'>
      <div id='debuginfo' style='overflow-x: auto'><table style='white-space: nowrap; margin: 0px' class='table table-condensed table-responsive table-bordered'>
<tbody>
<tr>
<td>Command</td>
<td>anomally_detector.py</td>
</tr>
<tr>
<td>Targets</td>
<td>/home/adrian/Desktop/TFM/Modelo/LOG_ERROR/log_fail1.log</td>
</tr>
<tr>
<td>Baselines</td>
<td>/home/adrian/Desktop/TFM/Modelo/LOG_OK/log_success1.log</td>
</tr>
<tr>
<td>Anomalies count</td>
<td>87</td>
</tr>
<tr>
<td>Run time</td>
<td>0.02 seconds</td>
</tr>
<tr>
<td>Reduction</td>
<td>72.22% (from 198 lines to 55)</td>
</tr>
</tbody></table><br /></div>
<div id='debuginfo' style='overflow-x: auto'><table style='white-space: nowrap; margin: 0px' class='table table-condensed table-responsive table-bordered'>
<thead><tr>
<th>Anomaly count</th>
<th>Filename</th>
<th>Test time</th>
<th>Model</th>
</tr></thead>
<tbody>
<tr>
<td>87</td>
<td><a href='#log_fail1.log'>log_fail1.log</a> (<a href='log_fail1.log'>log link</a>)</td>
<td>0.02 sec</td>
<td><a href='#model_log_success1.log'>log_success1.log</a></td>
</tr>
</tbody></table><br /></div>
<div class="list-group list-view-pf list-view-pf-view">

    <div class="list-group-item list-view-pf-expand-active" id='log_fail1.log'>
      <div class="list-group-item-header">
        <div class="list-view-pf-expand">
          <span class="fa fa-angle-right fa-angle-down"></span>
        </div>
        <div class="list-view-pf-main-info">
          <div class="list-view-pf-left">
            <span class="fa pficon-degraded list-view-pf-icon-sm"></span>
          </div>
          <div class="list-view-pf-body">
            <div class="list-view-pf-description">
              <div class="list-group-item-heading">
                log_fail1.log
              </div>
            </div>
            <div class="list-view-pf-additional-info-item" id='debuginfo'>
              <span class="pficon pficon-registry"></span>
              <a href="#model_log_success1.log">log_success1.log</a> model
            </div>
            <div class="list-view-pf-additional-info-item">
              <span class="fa fa-external-link"></span>
              <a href="log_fail1.log">file</a></strong>
            </div>
            <div class="list-view-pf-additional-info-item">
              <span class="fa fa-bug"></span>
              <strong>87</strong>
            </div>
          </div>
        </div>
      </div>
      <div class="list-group-item-container container-fluid">
        <div class="close"><span class="pficon pficon-close"></span></div>
        <div id='debuginfo'>baseline samples:<ul><li>/home/adrian/Desktop/TFM/Modelo/LOG_OK/log_success1.log</li></ul></div>
        <div class="loglines">
          <font color='#000000'>0.000 | 0002: 2021-09-30 09:11:25,494 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | INICIO registroDispensacion_eReceitaPeticionGenerica</font><br />
<font color='#000000'>0.000 | 0003: 2021-09-30 09:11:25,495 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | Peticin genrica :</font><br />
<font color='#590000'>0.349 | 0004: &lt;PeticionGenerica xmlns=&quot;http://disel/esquemas/peticionesyrespuestas&quot;&gt;  &lt;FechaHora xmlns=&quot;&quot;&gt;2021-09-30T09:11:25.489+02:00&lt;/FechaHora&gt;  &lt;IdTransaccion xmlns=&quot;&quot;&gt;358b2b31-899627169449&lt;/IdTransaccion&gt;  &lt;IP xmlns=&quot;&quot;&gt;192.168.200.211&lt;/IP&gt;  &lt;MensajePeticion xmlns=&quot;&quot;&gt;    &lt;EnClaro&gt;&lt;![CDATA[&lt;PeticionRegistroDispensacion_eReceita xmlns=&quot;http://disel/esquemas/peticionesyrespuestas&quot;&gt;  &lt;Cabecera xmlns=&quot;&quot;&gt;    &lt;Version&gt;3.0&lt;/Version&gt;    &lt;Software&gt;      &lt;FabricanteProducto&gt;DXC&lt;/FabricanteProducto&gt;      &lt;Version&gt;1.0&lt;/Version&gt;    &lt;/Software&gt;    &lt;FechaHora&gt;2021-09-30T09:11:25.487+02:00&lt;/FechaHora&gt;    &lt;IdFarmaceutico&gt;      &lt;NumeroColegiado&gt;45957561L&lt;/NumeroColegiado&gt;      &lt;NombreFarmaceutico&gt;LUCIA&lt;/NombreFarmaceutico&gt;      &lt;Apellidos&gt;RODRIGUEZ DOPICO&lt;/Apellidos&gt;    &lt;/IdFarmaceutico&gt;    &lt;IdFarmacia&gt;      &lt;CodigoNacionalFarmacia&gt;CO1062&lt;/CodigoNacionalFarmacia&gt;    &lt;/IdFarmacia&gt;    &lt;Idioma&gt;GA&lt;/Idioma&gt;    &lt;IP&gt;192.168.200.211&lt;/IP&gt;  &lt;/Cabecera&gt;  &lt;IdentificacionPaciente xmlns=&quot;&quot;&gt;    &lt;FuenteDatos&gt;manual&lt;/FuenteDatos&gt;    &lt;Documento&gt;540427SCIA0016&lt;/Documento&gt;    &lt;TipoDocumento&gt;CIP&lt;/TipoDocumento&gt;  &lt;/IdentificacionPaciente&gt;  &lt;RegistroDispensacion xmlns=&quot;&quot;&gt;    &lt;FechaDispensacion&gt;2021-09-30T09:11:25.486+02:00&lt;/FechaDispensacion&gt;    &lt;IdPrescripcion&gt;65521206&lt;/IdPrescripcion&gt;    &lt;IdReceta&gt;1172832314&lt;/IdReceta&gt;    &lt;ProductoDispensado&gt;      &lt;CodigoNacional&gt;915132&lt;/CodigoNacional&gt;      &lt;Prezomenor&gt;true&lt;/Prezomenor&gt;      &lt;NombreProducto&gt;SERC 16MG 30 COMPRIMIDOS&lt;/NombreProducto&gt;      &lt;TipoProducto&gt;medicamento&lt;/TipoProducto&gt;      &lt;EsPsicotropo&gt;false&lt;/EsPsicotropo&gt;      &lt;EsEstupefaciente&gt;false&lt;/EsEstupefaciente&gt;      &lt;DispensableEn&gt;A&lt;/DispensableEn&gt;      &lt;PVPNomenclator&gt;2.73&lt;/PVPNomenclator&gt;      &lt;PVPReal&gt;2.73&lt;/PVPReal&gt;      &lt;AportacionPaciente&gt;0.00&lt;/AportacionPaciente&gt;    &lt;/ProductoDispensado&gt;    &lt;NumeroEnvasesDispensados&gt;1&lt;/NumeroEnvasesDispensados&gt;    &lt;DispensacionForzada&gt;false&lt;/DispensacionForzada&gt;    &lt;LocalizacionCupon&gt;      &lt;NumeroPlantilla&gt;&lt;/NumeroPlantilla&gt;      &lt;CoordenadaX&gt;&lt;/CoordenadaX&gt;      &lt;CoordenadaY&gt;&lt;/CoordenadaY&gt;    &lt;/LocalizacionCupon&gt;    &lt;FirmaDispensacion&gt;      &lt;DocumentoFirmado&gt;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&lt;/DocumentoFirmado&gt;      &lt;Contenido&gt;&lt;![CDATA[&lt;DocFirmaDispensacion xmlns=&quot;http://disel/esquemas/DocumentosXMLFirma&quot;&gt;&lt;DocFirmaReceta xmlns=&quot;&quot;&gt;PABEAGEAdABvAHMARgBpAHIAbQBhAGQAbwBzAD4APABQAGEAYwBpAGUAbgB0AGUAPgA8AEMASQBQAD4ANQA0ADAANAAyADcAUwBDAEkAQQAwADAAMQA2ADwALwBDAEkAUAA+ADwATgBvAG0AYgByAGUAPgBDAEEAUgBNAEUATgA8AC8ATgBvAG0AYgByAGUAPgA8AEEAcABlAGwAbABpAGQAbwAxAD4AUwBJAEwAVgBBADwALwBBAHAAZQBsAGwAaQBkAG8AMQA+ADwAQQBwAGUAbABsAGkAZABvADIAPgBDAEEATQBCAEUASQBSAE8APAAvAEEAcABlAGwAbABpAGQAbwAyAD4APABGAGUAYwBoAGEATgBhAGMAaQBtAGkAZQBuAHQAbwA+ADEAOQA1ADQALQAwADQALQAyADcAPAAvAEYAZQBjAGgAYQBOAGEAYwBpAG0AaQBlAG4AdABvAD4APAAvAFAAYQBjAGkAZQBuAHQAZQA+ADwAUAByAGUAcwBjAHIAaQBwAGMAaQBvAG4APgA8AEkAZABQAHIAZQBzAGMAcgBpAHAAYwBpAG8AbgA+ADYANQA1ADIAMQAyADAANgA8AC8ASQBkAFAAcgBlAHMAYwByAGkAcABjAGkAbwBuAD4APABPAGIAagBlAHQAbwBQAHIAZQBzAGMAcgBpAHQAbwA+ADwARQBzAHAAZQBjAGkAYQBsAGkAZABhAGQAPgA8AEkAZABFAHMAcABlAGMAaQBhAGwAaQBkAGEAZAA+ADkAMQA1ADEAMwAyADwALwBJAGQARQBzAHAAZQBjAGkAYQBsAGkAZABhAGQAPgA8AEQAZQBzAGMAcgBpAHAARQBzAHAAZQBjAGkAYQBsAGkAZABhAGQAPgBTAEUAUgBDACAAMQA2AE0ARwAgADMAMAAgAEMATwBNAFAAUgBJAE0ASQBEAE8AUwA8AC8ARABlAHMAYwByAGkAcABFAHMAcABlAGMAaQBhAGwAaQBkAGEAZAA+ADwALwBFAHMAcABlAGMAaQBhAGwAaQBkAGEAZAA+ADwALwBPAGIAagBlAHQAbwBQAHIAZQBzAGMAcgBpAHQAbwA+ADwAUwBlAGwAbABvAEMAYQBtAHAAUwBhAG4AaQB0AD4AMAA8AC8AUwBlAGwAbABvAEMAYQBtAHAAUwBhAG4AaQB0AD4APABQAGUAcgBpAG8AZABvAFIAZQBjAGUAdABhAGQAbwA+ADwAUgBlAGMAZQB0AGEAPgA8AEkAZABSAGUAYwBlAHQAYQA+ADEAMQA3ADIAOAAzADIAMwAxADQAPAAvAEkAZABSAGUAYwBlAHQAYQA+ADwARABlAHMAYwByAGkAcABUAGkAcABvAFIAZQBjAGUAdABhAD4AUABFAE4AUwBJAE8ATgBJAFMAVABBADwALwBEAGUAcwBjAHIAaQBwAFQAaQBwAG8AUgBlAGMAZQB0AGEAPgA8AFAAbwBzAG8AbABvAGcAaQBhAD4APABQAG8AcwBvAGwAbwBnAGkAYQBHAGUAbgBlAHIAYQBsAD4APABEAG8AcwBpAHMAPgAxADwALwBEAG8AcwBpAHMAPgA8AFUAbgBpAGQAYQBkAGUAcwA+AEMATwBNAFAAUgBJAE0ASQBEAE8AUwA8AC8AVQBuAGkAZABhAGQAZQBzAD4APABDAGEAZABhAD4AOAA8AC8AQwBhAGQAYQA+ADwAQwBvAGQAVQBkAHMAQwBhAGQAYQA+AEgAPAAvAEMAbwBkAFUAZABzAEMAYQBkAGEAPgA8AC8AUABvAHMAbwBsAG8AZwBpAGEARwBlAG4AZQByAGEAbAA+ADwALwBQAG8AcwBvAGwAbwBnAGkAYQA+ADwATgB1AG0ARQBuAHYAYQBzAGUAcwA+ADEAPAAvAE4AdQBtAEUAbgB2AGEAcwBlAHMAPgA8AEkAbgBzAHQAcgB1AGMAYwBpAG8AbgBlAHMAUABhAGMAaQBlAG4AdABlAD4APAAvAEkAbgBzAHQAcgB1AGMAYwBpAG8AbgBlAHMAUABhAGMAaQBlAG4AdABlAD4APABBAGQAdgBlAHIAdABlAG4AYwBpAGEAcwA+ADwALwBBAGQAdgBlAHIAdABlAG4AYwBpAGEAcwA+ADwARgBlAGMAaABhAEQAaQBzAHAAZQBuAHMAYQBjAGkAbwBuAFAAcgBlAHYAaQBzAHQAYQA+ADIAMAAyADEALQAxADAALQAwADcAPAAvAEYAZQBjAGgAYQBEAGkAcwBwAGUAbgBzAGEAYwBpAG8AbgBQAHIAZQB2AGkAcwB0AGEAPgA8AFIAZQBxAHUAaQBlAHIAZQBIAG8AbQBvAGwAbwBnAGEAYwBpAG8AbgA+AGYAYQBsAHMAZQA8AC8AUgBlAHEAdQBpAGUAcgBlAEgAbwBtAG8AbABvAGcAYQBjAGkAbwBuAD4APABGAGEAYwB1AGwAdABhAHQAaQB2AG8APgA8AEMATgBQAD4ANAA4ADAAOQA0ADUAPAAvAEMATgBQAD4APABOAG8AbQBiAHIAZQA+AE0AQQBOAFUARQBMADwALwBOAG8AbQBiAHIAZQA+ADwAQQBwAGUAbABsAGkAZABvADEAPgBNAEkATABMAEEATgA8AC8AQQBwAGUAbABsAGkAZABvADEAPgA8AEEAcABlAGwAbABpAGQAbwAyAD4ATQBBAFIASQDRAE8APAAvAEEAcABlAGwAbABpAGQAbwAyAD4APABEAGUAcwBjAHIAaQBwAEMAZQBuAHQAcgBvAD4AQwBFAE4AVABSAE8AIABTAEEAVQBEAEUAIABDAEEATQBBAFIASQDRAEEAUwA8AC8ARABlAHMAYwByAGkAcABDAGUAbgB0AHIAbwA+ADwATgB1AG0AQwBvAGwAZQBnAGkAYQBkAG8APgAxADUAMAA2ADcAMgAwADMAPAAvAE4AdQBtAEMAbwBsAGUAZwBpAGEAZABvAD4APAAvAEYAYQBjAHUAbAB0AGEAdABpAHYAbwA+ADwARgBlAGMAaABhAEMAcgBlAGEAYwBpAG8AbgA+ADIAMAAyADEALQAwADQALQAyADYAVAAwADAAOgAwADAAOgAwADAAPAAvAEYAZQBjAGgAYQBDAHIAZQBhAGMAaQBvAG4APgA8AC8AUgBlAGMAZQB0AGEAPgA8AC8AUABlAHIAaQBvAGQAbwBSAGUAYwBlAHQAYQBkAG8APgA8AEQAZQBzAGMAcgBpAHAAVgBpAGEAPgBPAFIAQQBMADwALwBEAGUAcwBjAHIAaQBwAFYAaQBhAD4APABEAHUAcgBhAGMAaQBvAG4AVAByAGEAdABhAG0AaQBlAG4AdABvAD4APAAvAEQAdQByAGEAYwBpAG8AbgBUAHIAYQB0AGEAbQBpAGUAbgB0AG8APgA8AFUAbgBpAGQAYQBkAEQAdQByAGEAYwBpAG8AbgBUAHIAYQB0AGEAbQBpAGUAbgB0AG8APgA8AC8AVQBuAGkAZABhAGQARAB1AHIAYQBjAGkAbwBuAFQAcgBhAHQAYQBtAGkAZQBuAHQAbwA+ADwALwBQAHIAZQBzAGMAcgBpAHAAYwBpAG8AbgA+ADwALwBEAGEAdABvAHMARgBpAHIAbQBhAGQAbwBzAD4A&lt;/DocFirmaReceta&gt;&lt;FirmaFacultativoEmisor xmlns=&quot;&quot;&gt;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&lt;/FirmaFacultativoEmisor&gt;&lt;DatosPropiosDispensacion xmlns=&quot;&quot;&gt;&lt;FechaDispensacion&gt;2021-09-30T09:11:07.668+02:00&lt;/FechaDispensacion&gt;&lt;IdentificacionFarmaceuticoDispensador&gt;&lt;NumeroColegiado&gt;45957561L&lt;/NumeroColegiado&gt;&lt;NombreFarmaceutico&gt;LUCIA&lt;/NombreFarmaceutico&gt;&lt;Apellidos&gt;RODRIGUEZ DOPICO&lt;/Apellidos&gt;&lt;/IdentificacionFarmaceuticoDispensador&gt;&lt;CampanaSanitaria&gt;false&lt;/CampanaSanitaria&gt;&lt;NIF_RecogeDispensacion&gt;&lt;/NIF_RecogeDispensacion&gt;&lt;IdentificacionFarmacia&gt;&lt;CodigoNacionalFarmacia&gt;CO1062&lt;/CodigoNacionalFarmacia&gt;&lt;/IdentificacionFarmacia&gt;&lt;ProductoDispensado&gt;&lt;CodigoNacional&gt;915132&lt;/CodigoNacional&gt;&lt;NombreProducto&gt;SERC 16MG 30 COMPRIMIDOS&lt;/NombreProducto&gt;&lt;TipoProducto&gt;medicamento&lt;/TipoProducto&gt;&lt;EsPsicotropo&gt;false&lt;/EsPsicotropo&gt;&lt;EsEstupefaciente&gt;false&lt;/EsEstupefaciente&gt;&lt;PVPNomenclator&gt;2.73&lt;/PVPNomenclator&gt;&lt;AportacionPaciente&gt;0.00&lt;/AportacionPaciente&gt;&lt;/ProductoDispensado&gt;&lt;NumeroEnvasesDispensados&gt;1&lt;/NumeroEnvasesDispensados&gt;&lt;ExpedicionReceta&gt;&lt;Es_eReceita&gt;true&lt;/Es_eReceita&gt;&lt;EsImpresa&gt;false&lt;/EsImpresa&gt;&lt;/ExpedicionReceta&gt;&lt;DispensacionForzada&gt;false&lt;/DispensacionForzada&gt;&lt;DispensacionCDR&gt;false&lt;/DispensacionCDR&gt;&lt;TipoRecetaDispensada&gt;R_pensionista_roja&lt;/TipoRecetaDispensada&gt;&lt;TipoAportacionDispensacion&gt;&lt;TipoReceta&gt;R_pensionista_roja&lt;/TipoReceta&gt;&lt;AportacionTotalReceta&gt;0.0&lt;/AportacionTotalReceta&gt;&lt;/TipoAportacionDispensacion&gt;&lt;/DatosPropiosDispensacion&gt;&lt;/DocFirmaDispensacion&gt;]]]]&gt;&gt;&lt;![CDATA[&lt;/Contenido&gt;    &lt;/FirmaDispensacion&gt;    &lt;TipoAportacion&gt;      &lt;TipoReceta&gt;TSI 001&lt;/TipoReceta&gt;      &lt;AportacionTotalReceta&gt;0.0&lt;/AportacionTotalReceta&gt;    &lt;/TipoAportacion&gt;  &lt;/RegistroDispensacion&gt;&lt;/PeticionRegistroDispensacion_eReceita&gt;]]&gt;&lt;/EnClaro&gt;  &lt;/MensajePeticion&gt;&lt;/PeticionGenerica&gt;</font><br />
<font color='#000000'>0.000 | 0005: 2021-09-30 09:11:25,496 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | INICIO registroDispensacion_eReceita</font><br />
<hr class='ls' />
<font color='#000000'>0.000 | 0049:     &lt;FechaHora&gt;2021-09-30T09:11:25.487+02:00&lt;/FechaHora&gt;</font><br />
<font color='#000000'>0.000 | 0050:     &lt;IdFarmaceutico&gt;</font><br />
<font color='#000000'>0.000 | 0051:       &lt;NumeroColegiado&gt;45957561L&lt;/NumeroColegiado&gt;</font><br />
<font color='#540000'>0.333 | 0052:       &lt;NombreFarmaceutico&gt;LUCIA&lt;/NombreFarmaceutico&gt;</font><br />
<font color='#8c0000'>0.553 | 0053:       &lt;Apellidos&gt;RODRIGUEZ DOPICO&lt;/Apellidos&gt;</font><br />
<font color='#000000'>0.000 | 0054:     &lt;/IdFarmaceutico&gt;</font><br />
<hr class='ls' />
<font color='#000000'>0.000 | 0060:   &lt;/Cabecera&gt;</font><br />
<font color='#000000'>0.000 | 0061:   &lt;IdentificacionPaciente&gt;</font><br />
<font color='#000000'>0.000 | 0062:     &lt;FuenteDatos&gt;manual&lt;/FuenteDatos&gt;</font><br />
<font color='#540000'>0.333 | 0063:     &lt;Documento&gt;540427SCIA0016&lt;/Documento&gt;</font><br />
<font color='#000000'>0.000 | 0064:     &lt;TipoDocumento&gt;CIP&lt;/TipoDocumento&gt;</font><br />
<hr class='ls' />
<font color='#000000'>0.000 | 0124: 2021-09-30 09:11:25,852 | INFO  | BLServicioValidacionFarmacia | [358b2b31-899627169449] | FIN validacion</font><br />
<font color='#000000'>0.000 | 0125: 2021-09-30 09:11:25,852 | INFO  | RegistroDispensacionActionDelegate$RegistroDispensacionIndividualActionDelegate | [358b2b31-899627169449] | Verificando firma...</font><br />
<font color='#000000'>0.000 | 0126: 2021-09-30 09:11:25,853 | INFO  | RegistroDispensacionActionDelegate$RegistroDispensacionIndividualActionDelegate | [358b2b31-899627169449] | Firma Detached</font><br />
<font color='#9c0000'>0.613 | 0127: 2021-09-30 09:11:25,862 | INFO  | BLServicioDispensacionesFarmacia | [358b2b31-899627169449] | Se ha obtenido un error durante la dispensacin, se procede a deshacer los IU anteriormente desactivados</font><br />
<font color='#320000'>0.200 | 0128: 2021-09-30 09:11:25,862 | INFO  | BLServicioDispensacionesFarmacia | [358b2b31-899627169449] | INICIO: deshacerDispensacionIdentificadoresUnicos</font><br />
<font color='#3f0000'>0.250 | 0129: 2021-09-30 09:11:25,862 | INFO  | BLServicioDispensacionesFarmacia | [358b2b31-899627169449] | FIN: deshacerDispensacionIdentificadoresUnicos</font><br />
<font color='#9c0000'>0.613 | 0130: 2021-09-30 09:11:25,862 | ERROR | RegistroDispensacionActionDelegate$RegistroDispensacionIndividualActionDelegate | [358b2b31-899627169449] | Excepcion capturada: </font><br />
<font color='#ff0000'>1.000 | 0131: es.sergas.disel.recursos.exception.DiselException</font><br />
<font color='#bd0000'>0.742 | 0132: 	at es.sergas.disel.plataforma.businesslogic.dispensaciones.actiondelegate.RegistroDispensacionActionDelegate$RegistroDispensacionIndividualActionDelegate.tratarPeticionDispensacionConFirma(RegistroDispensacionActionDelegate.java:1328)</font><br />
<font color='#bd0000'>0.742 | 0133: 	at es.sergas.disel.plataforma.businesslogic.dispensaciones.actiondelegate.RegistroDispensacionActionDelegate$RegistroDispensacionIndividualActionDelegate.registroDispensacion_eReceitaIndividual(RegistroDispensacionActionDelegate.java:564)</font><br />
<font color='#d40000'>0.833 | 0134: 	at es.sergas.disel.plataforma.businesslogic.dispensaciones.actiondelegate.RegistroDispensacionActionDelegate.registroDispensacion_eReceita(RegistroDispensacionActionDelegate.java:261)</font><br />
<font color='#a40000'>0.646 | 0135: 	at es.sergas.disel.plataforma.businesslogic.dispensaciones.BLServicioDispensacionesFarmacia.registroDispensacion_eReceita(BLServicioDispensacionesFarmacia.java:3578)</font><br />
<font color='#a40000'>0.646 | 0136: 	at es.sergas.disel.plataforma.operationflow.dispensacion.OFServicioDispensacionesAC.registroDispensacion_eReceita(OFServicioDispensacionesAC.java:1457)</font><br />
<font color='#a40000'>0.646 | 0137: 	at es.sergas.disel.plataforma.operationflow.dispensacion.OFServicioDispensacionesAC.registroDispensacion_eReceitaPeticionGenerica(OFServicioDispensacionesAC.java:1385)</font><br />
<font color='#c20000'>0.764 | 0138: 	at es.sergas.disel.plataforma.servicios.dispensacion.BindingServicioDispensacionesACImpl.registroDispensacion_eReceitaAC(BindingServicioDispensacionesACImpl.java:364)</font><br />
<font color='#dc0000'>0.864 | 0139: 	at sun.reflect.GeneratedMethodAccessor2599.invoke(Unknown Source)</font><br />
<font color='#d80000'>0.851 | 0140: 	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:37)</font><br />
<font color='#de0000'>0.871 | 0141: 	at java.lang.reflect.Method.invoke(Method.java:611)</font><br />
<font color='#ff0000'>1.000 | 0142: 	at com.ibm.ws.webservices.engine.dispatchers.java.JavaDispatcher.invokeMethod(JavaDispatcher.java:203)</font><br />
<font color='#ff0000'>1.000 | 0143: 	at com.ibm.ws.webservices.engine.dispatchers.java.JavaDispatcher.invokeOperation(JavaDispatcher.java:158)</font><br />
<font color='#ff0000'>1.000 | 0144: 	at com.ibm.ws.webservices.engine.dispatchers.SoapRPCProcessor.processRequestResponse(SoapRPCProcessor.java:490)</font><br />
<font color='#ff0000'>1.000 | 0145: 	at com.ibm.ws.webservices.engine.dispatchers.SoapRPCProcessor.processMessage(SoapRPCProcessor.java:433)</font><br />
<font color='#ff0000'>1.000 | 0146: 	at com.ibm.ws.webservices.engine.dispatchers.BasicDispatcher.processMessage(BasicDispatcher.java:134)</font><br />
<font color='#e00000'>0.882 | 0147: 	at com.ibm.ws.webservices.engine.dispatchers.java.SessionDispatcher.invoke(SessionDispatcher.java:204)</font><br />
<font color='#de0000'>0.871 | 0148: 	at com.ibm.ws.webservices.engine.PivotHandlerWrapper.invoke(PivotHandlerWrapper.java:264)</font><br />
<font color='#e30000'>0.891 | 0149: 	at com.ibm.ws.webservices.engine.handlers.jaxrpc.JAXRPCHandler.invoke(JAXRPCHandler.java:153)</font><br />
<font color='#e00000'>0.882 | 0150: 	at com.ibm.ws.webservices.engine.handlers.WrappedHandler.invoke(WrappedHandler.java:64)</font><br />
<font color='#000000'>0.000 | 0151: 	at com.ibm.ws.webservices.engine.PivotHandlerWrapper.invoke(PivotHandlerWrapper.java:264)</font><br />
<font color='#000000'>0.000 | 0152: 	at com.ibm.ws.webservices.engine.PivotHandlerWrapper.invoke(PivotHandlerWrapper.java:264)</font><br />
<font color='#de0000'>0.871 | 0153: 	at com.ibm.ws.webservices.engine.WebServicesEngine.invoke(WebServicesEngine.java:336)</font><br />
<font color='#da0000'>0.857 | 0154: 	at com.ibm.ws.webservices.engine.transport.http.WebServicesServlet.doPost(WebServicesServlet.java:1239)</font><br />
<font color='#d70000'>0.846 | 0155: 	at javax.servlet.http.HttpServlet.service(HttpServlet.java:595)</font><br />
<font color='#da0000'>0.857 | 0156: 	at com.ibm.ws.webservices.engine.transport.http.WebServicesServletBase.service(WebServicesServletBase.java:344)</font><br />
<font color='#000000'>0.000 | 0157: 	at javax.servlet.http.HttpServlet.service(HttpServlet.java:668)</font><br />
<font color='#ff0000'>1.000 | 0158: 	at com.ibm.ws.webcontainer.servlet.ServletWrapper.service(ServletWrapper.java:1233)</font><br />
<font color='#ff0000'>1.000 | 0159: 	at com.ibm.ws.webcontainer.servlet.ServletWrapper.handleRequest(ServletWrapper.java:782)</font><br />
<font color='#000000'>0.000 | 0160: 	at com.ibm.ws.webcontainer.servlet.ServletWrapper.handleRequest(ServletWrapper.java:481)</font><br />
<font color='#ff0000'>1.000 | 0161: 	at com.ibm.ws.webcontainer.servlet.ServletWrapperImpl.handleRequest(ServletWrapperImpl.java:178)</font><br />
<font color='#ff0000'>1.000 | 0162: 	at com.ibm.ws.webcontainer.filter.WebAppFilterManager.invokeFilters(WebAppFilterManager.java:1114)</font><br />
<font color='#ff0000'>1.000 | 0163: 	at com.ibm.ws.webcontainer.servlet.CacheServletWrapper.handleRequest(CacheServletWrapper.java:87)</font><br />
<font color='#ff0000'>1.000 | 0164: 	at com.ibm.ws.webcontainer.WebContainer.handleRequest(WebContainer.java:949)</font><br />
<font color='#ff0000'>1.000 | 0165: 	at com.ibm.ws.webcontainer.WSWebContainer.handleRequest(WSWebContainer.java:1817)</font><br />
<font color='#ff0000'>1.000 | 0166: 	at com.ibm.ws.webcontainer.channel.WCChannelLink.ready(WCChannelLink.java:200)</font><br />
<font color='#da0000'>0.857 | 0167: 	at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.handleDiscrimination(HttpInboundLink.java:463)</font><br />
<font color='#da0000'>0.857 | 0168: 	at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.handleNewRequest(HttpInboundLink.java:530)</font><br />
<font color='#da0000'>0.857 | 0169: 	at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.processRequest(HttpInboundLink.java:316)</font><br />
<font color='#da0000'>0.857 | 0170: 	at com.ibm.ws.http.channel.inbound.impl.HttpICLReadCallback.complete(HttpICLReadCallback.java:88)</font><br />
<font color='#ff0000'>1.000 | 0171: 	at com.ibm.ws.tcp.channel.impl.AioReadCompletionListener.futureCompleted(AioReadCompletionListener.java:175)</font><br />
<font color='#ff0000'>1.000 | 0172: 	at com.ibm.io.async.AbstractAsyncFuture.invokeCallback(AbstractAsyncFuture.java:217)</font><br />
<font color='#ff0000'>1.000 | 0173: 	at com.ibm.io.async.AsyncChannelFuture.fireCompletionActions(AsyncChannelFuture.java:161)</font><br />
<font color='#ff0000'>1.000 | 0174: 	at com.ibm.io.async.AsyncFuture.completed(AsyncFuture.java:138)</font><br />
<font color='#ff0000'>1.000 | 0175: 	at com.ibm.io.async.ResultHandler.complete(ResultHandler.java:204)</font><br />
<font color='#ff0000'>1.000 | 0176: 	at com.ibm.io.async.ResultHandler.runEventProcessingLoop(ResultHandler.java:775)</font><br />
<font color='#ff0000'>1.000 | 0177: 	at com.ibm.io.async.ResultHandler$2.run(ResultHandler.java:905)</font><br />
<font color='#ff0000'>1.000 | 0178: 	at com.ibm.ws.util.ThreadPool$Worker.run(ThreadPool.java:1892)</font><br />
<font color='#000000'>0.000 | 0179: 2021-09-30 09:11:25,863 | INFO  | BLServicioDispensacionesFarmacia | [358b2b31-899627169449] | FIN registroDispensacion_eReceita</font><br />
<font color='#000000'>0.000 | 0180: 2021-09-30 09:11:25,864 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | FIN registroDispensacion_eReceita</font><br />
<font color='#000000'>0.000 | 0181: 2021-09-30 09:11:25,864 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | Respuesta Peticin: </font><br />
<font color='#000000'>0.000 | 0182: &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;</font><br />
<font color='#3e0000'>0.244 | 0183: &lt;RespuestaRegistroDispensacion_eReceita xmlns=&quot;http://disel/esquemas/peticionesyrespuestas&quot;&gt;</font><br />
<font color='#000000'>0.000 | 0184:   &lt;ConfirmacionRegistroDispensacion xmlns=&quot;&quot;&gt;</font><br />
<hr class='ls' />
<font color='#000000'>0.000 | 0186:     &lt;RespuestaOperacion&gt;</font><br />
<font color='#000000'>0.000 | 0187:       &lt;FechaHora&gt;2021-09-30T09:11:25.863+02:00&lt;/FechaHora&gt;</font><br />
<font color='#000000'>0.000 | 0188:       &lt;CodigoRespuesta&gt;SD0015&lt;/CodigoRespuesta&gt;</font><br />
<font color='#980000'>0.600 | 0189:       &lt;DescripcionCorta&gt;Erro na sinatura da operacin.&lt;/DescripcionCorta&gt;</font><br />
<font color='#ae0000'>0.684 | 0190:       &lt;Descripcion&gt;Non coincide o certificado do asinante (32621235J) co farmacutico rexistrado na aplicacin (45957561L).&lt;/Descripcion&gt;</font><br />
<font color='#000000'>0.000 | 0191:     &lt;/RespuestaOperacion&gt;</font><br />
<hr class='ls' />
<font color='#000000'>0.000 | 0193: &lt;/RespuestaRegistroDispensacion_eReceita&gt;</font><br />
<font color='#000000'>0.000 | 0194: 2021-09-30 09:11:25,864 | INFO  | DiselPlataformaUtils | [358b2b31-899627169449] | inicio generarMsjeRptaGenericaRegDisp</font><br />
<font color='#000000'>0.000 | 0195: 2021-09-30 09:11:25,864 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | Respuesta genrica :</font><br />
<font color='#3e0000'>0.246 | 0196: &lt;RespuestaGenerica xmlns=&quot;http://disel/esquemas/peticionesyrespuestas&quot;&gt;  &lt;FechaHora xmlns=&quot;&quot;&gt;2021-09-30T09:11:25.864+02:00&lt;/FechaHora&gt;  &lt;IdTransaccion xmlns=&quot;&quot;&gt;358b2b31-899627169449&lt;/IdTransaccion&gt;  &lt;MensajeRespuesta xmlns=&quot;&quot;&gt;    &lt;EnClaro&gt;&lt;![CDATA[&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&lt;RespuestaRegistroDispensacion_eReceita xmlns=&quot;http://disel/esquemas/peticionesyrespuestas&quot;&gt;  &lt;ConfirmacionRegistroDispensacion xmlns=&quot;&quot;&gt;    &lt;IdReceta&gt;1172832314&lt;/IdReceta&gt;    &lt;RespuestaOperacion&gt;      &lt;FechaHora&gt;2021-09-30T09:11:25.863+02:00&lt;/FechaHora&gt;      &lt;CodigoRespuesta&gt;SD0015&lt;/CodigoRespuesta&gt;      &lt;DescripcionCorta&gt;Erro na sinatura da operacin.&lt;/DescripcionCorta&gt;      &lt;Descripcion&gt;Non coincide o certificado do asinante (32621235J) co farmacutico rexistrado na aplicacin (45957561L).&lt;/Descripcion&gt;    &lt;/RespuestaOperacion&gt;  &lt;/ConfirmacionRegistroDispensacion&gt;&lt;/RespuestaRegistroDispensacion_eReceita&gt;]]&gt;&lt;/EnClaro&gt;  &lt;/MensajeRespuesta&gt;  &lt;RespuestaOperacion xmlns=&quot;&quot;&gt;    &lt;FechaHora&gt;2021-09-30T09:11:25.864+02:00&lt;/FechaHora&gt;    &lt;CodigoRespuesta&gt;NE0000&lt;/CodigoRespuesta&gt;    &lt;DescripcionCorta&gt;Operacin realizada con exito&lt;/DescripcionCorta&gt;    &lt;Descripcion&gt;Operacin realizada con xito&lt;/Descripcion&gt;  &lt;/RespuestaOperacion&gt;&lt;/RespuestaGenerica&gt;</font><br />
<font color='#000000'>0.000 | 0197: 2021-09-30 09:11:25,864 | INFO  | OFServicioDispensacionesAC | [358b2b31-899627169449] | FIN registroDispensacion_eReceitaPeticionGenerica</font><br />
        </div>
      </div>
    </div>
    
</div>
<div id='debuginfo' style='overflow-x: auto'><table style='white-space: nowrap; margin: 0px' class='table table-condensed table-responsive table-bordered'>
<thead><tr>
<th>Model</th>
<th>Train time</th>
<th>Infos</th>
<th>Baseline files</th>
</tr></thead>
<tbody>
<tr id='model_log_success1.log'>
<td>log_success1.log</td>
<td>0.00 sec</td>
<td>153 samples, 262144 features</td>
<td>/home/adrian/Desktop/TFM/Modelo/LOG_OK/log_success1.log</td>
</tr>
</tbody></table><br /></div>
    </div>
    <script src='https://code.jquery.com/jquery-3.3.1.min.js'></script>
    <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/patternfly/3.24.0/js/patternfly.min.js'></script>
    <script>
$(document).ready(function(){
$('#debugbtn').on('click', function(event) {$('[id=debuginfo]').toggle();});
});
$(".list-group-item-header").click(function(event){
  if(!$(event.target).is("button, a, input, .fa-ellipsis-v")){
    $(this).find(".fa-angle-right").toggleClass("fa-angle-down")
      .end().parent().toggleClass("list-view-pf-expand-active")
      .find(".list-group-item-container").toggleClass("hidden");
    }
})
$(".list-group-item-container .close").on("click", function (){
  $(this).parent().addClass("hidden")
         .parent().removeClass("list-view-pf-expand-active")
         .find(".fa-angle-right").removeClass("fa-angle-down");
})
</script>
  </body>
</html>

    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login('testalertingtfm@outlook.es', 'testAlerting22')
    server.sendmail('testalertingtfm@outlook.es', 'testalertingtfm@outlook.es', message.as_string())

    client = MongoClient("mongodb://mongo:mongo@127.0.0.1:27017")
    mydb = client["alerting"]
    mycol = mydb["alert"]

    mydict = {"type": "unknown", "text": "prueba", "date" : datetime.now()}

    x = mycol.insert_one(mydict)
    client.close

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
