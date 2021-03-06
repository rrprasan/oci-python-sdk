# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConfigSourceDetails(object):
    """
    Property details for the configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConfigSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.CreateZipUploadConfigSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateConfigSourceDetails.
        :type working_directory: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory'
        }

        self._config_source_type = None
        self._working_directory = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configSourceType']

        if type == 'ZIP_UPLOAD':
            return 'CreateZipUploadConfigSourceDetails'
        else:
            return 'CreateConfigSourceDetails'

    @property
    def config_source_type(self):
        """
        **[Required]** Gets the config_source_type of this CreateConfigSourceDetails.
        The configuration file type.


        :return: The config_source_type of this CreateConfigSourceDetails.
        :rtype: str
        """
        return self._config_source_type

    @config_source_type.setter
    def config_source_type(self, config_source_type):
        """
        Sets the config_source_type of this CreateConfigSourceDetails.
        The configuration file type.


        :param config_source_type: The config_source_type of this CreateConfigSourceDetails.
        :type: str
        """
        self._config_source_type = config_source_type

    @property
    def working_directory(self):
        """
        Gets the working_directory of this CreateConfigSourceDetails.
        File path to the directory from which Terraform runs.
        If not specified, the root directory is used.


        :return: The working_directory of this CreateConfigSourceDetails.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this CreateConfigSourceDetails.
        File path to the directory from which Terraform runs.
        If not specified, the root directory is used.


        :param working_directory: The working_directory of this CreateConfigSourceDetails.
        :type: str
        """
        self._working_directory = working_directory

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
