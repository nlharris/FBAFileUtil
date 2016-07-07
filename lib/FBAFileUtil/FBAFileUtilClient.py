############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class FBAFileUtil(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def excel_file_to_model(self, p, context=None):
        """
        :param p: instance of type "ModelCreationParams" (compounds_file is
           not used for excel file creations) -> structure: parameter
           "model_file" of type "File" -> structure: parameter "path" of
           String, parameter "model_name" of String, parameter
           "workspace_name" of String, parameter "genome" of String,
           parameter "biomass" of list of String, parameter "compounds_file"
           of type "File" -> structure: parameter "path" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.excel_file_to_model',
            [p], self._service_ver, context)

    def sbml_file_to_model(self, p, context=None):
        """
        :param p: instance of type "ModelCreationParams" (compounds_file is
           not used for excel file creations) -> structure: parameter
           "model_file" of type "File" -> structure: parameter "path" of
           String, parameter "model_name" of String, parameter
           "workspace_name" of String, parameter "genome" of String,
           parameter "biomass" of list of String, parameter "compounds_file"
           of type "File" -> structure: parameter "path" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.sbml_file_to_model',
            [p], self._service_ver, context)

    def tsv_file_to_model(self, p, context=None):
        """
        :param p: instance of type "ModelCreationParams" (compounds_file is
           not used for excel file creations) -> structure: parameter
           "model_file" of type "File" -> structure: parameter "path" of
           String, parameter "model_name" of String, parameter
           "workspace_name" of String, parameter "genome" of String,
           parameter "biomass" of list of String, parameter "compounds_file"
           of type "File" -> structure: parameter "path" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.tsv_file_to_model',
            [p], self._service_ver, context)

    def model_to_excel_file(self, model, context=None):
        """
        :param model: instance of type "ModelObjectSelection" -> structure:
           parameter "workspace_name" of String, parameter "model_name" of
           String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.model_to_excel_file',
            [model], self._service_ver, context)

    def model_to_sbml_file(self, model, context=None):
        """
        :param model: instance of type "ModelObjectSelection" -> structure:
           parameter "workspace_name" of String, parameter "model_name" of
           String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.model_to_sbml_file',
            [model], self._service_ver, context)

    def model_to_tsv_file(self, model, context=None):
        """
        :param model: instance of type "ModelObjectSelection" -> structure:
           parameter "workspace_name" of String, parameter "model_name" of
           String
        :returns: instance of type "ModelTsvFiles" -> structure: parameter
           "compounds_file" of type "File" -> structure: parameter "path" of
           String, parameter "reactions_file" of type "File" -> structure:
           parameter "path" of String
        """
        return self._client.call_method(
            'FBAFileUtil.model_to_tsv_file',
            [model], self._service_ver, context)

    def fba_to_excel_file(self, fba, context=None):
        """
        :param fba: instance of type "FBAObjectSelection" (****** FBA Result
           Converters ******) -> structure: parameter "workspace_name" of
           String, parameter "fba_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.fba_to_excel_file',
            [fba], self._service_ver, context)

    def fba_to_tsv_file(self, fba, context=None):
        """
        :param fba: instance of type "FBAObjectSelection" (****** FBA Result
           Converters ******) -> structure: parameter "workspace_name" of
           String, parameter "fba_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.fba_to_tsv_file',
            [fba], self._service_ver, context)

    def tsv_file_to_media(self, p, context=None):
        """
        :param p: instance of type "MediaCreationParams" (****** Media
           Converters *********) -> structure: parameter "media_file" of type
           "File" -> structure: parameter "path" of String, parameter
           "media_name" of String, parameter "workspace_name" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.tsv_file_to_media',
            [p], self._service_ver, context)

    def excel_file_to_media(self, p, context=None):
        """
        :param p: instance of type "MediaCreationParams" (****** Media
           Converters *********) -> structure: parameter "media_file" of type
           "File" -> structure: parameter "path" of String, parameter
           "media_name" of String, parameter "workspace_name" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.excel_file_to_media',
            [p], self._service_ver, context)

    def media_to_tsv_file(self, media, context=None):
        """
        :param media: instance of type "MediaObjectSelection" -> structure:
           parameter "workspace_name" of String, parameter "media_name" of
           String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.media_to_tsv_file',
            [media], self._service_ver, context)

    def media_to_excel_file(self, media, context=None):
        """
        :param media: instance of type "MediaObjectSelection" -> structure:
           parameter "workspace_name" of String, parameter "media_name" of
           String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.media_to_excel_file',
            [media], self._service_ver, context)

    def tsv_file_to_phenotype_set(self, p, context=None):
        """
        :param p: instance of type "PhenotypeCreationParams" (******
           Phenotype Data Converters *******) -> structure: parameter
           "phenotype_file" of type "File" -> structure: parameter "path" of
           String, parameter "phenotype_name" of String, parameter
           "workspace_name" of String, parameter "genome" of String
        :returns: instance of type "WorkspaceRef" -> structure: parameter
           "ref" of String
        """
        return self._client.call_method(
            'FBAFileUtil.tsv_file_to_phenotype_set',
            [p], self._service_ver, context)

    def phenotype_set_to_tsv_file(self, phenotype, context=None):
        """
        :param phenotype: instance of type "PhenotypeObjectSelection" ->
           structure: parameter "workspace_name" of String, parameter
           "phenotype_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.phenotype_set_to_tsv_file',
            [phenotype], self._service_ver, context)

    def phenotype_simulation_set_to_excel_file(self, pss, context=None):
        """
        :param pss: instance of type "PhenotypeSetObjectSelection" ->
           structure: parameter "workspace_name" of String, parameter
           "phenotype_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.phenotype_simulation_set_to_excel_file',
            [pss], self._service_ver, context)

    def phenotype_simulation_set_to_tsv_file(self, pss, context=None):
        """
        :param pss: instance of type "PhenotypeSetObjectSelection" ->
           structure: parameter "workspace_name" of String, parameter
           "phenotype_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.phenotype_simulation_set_to_tsv_file',
            [pss], self._service_ver, context)

    def phenotype_simulation_set_to_excel_file(self, pss, context=None):
        """
        :param pss: instance of type "PhenotypeSetObjectSelection" ->
           structure: parameter "workspace_name" of String, parameter
           "phenotype_name" of String
        :returns: instance of type "File" -> structure: parameter "path" of
           String
        """
        return self._client.call_method(
            'FBAFileUtil.phenotype_simulation_set_to_excel_file',
            [pss], self._service_ver, context)
