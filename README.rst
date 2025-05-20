LTI Launch Monitor
##################

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

This is a plugin for edx-platform that hooks into events related to LTI Provider
Launches and records the events to the database.

Getting Started with Development
********************************

In order to develop this plugin, you can mount it in tutor and it shoudl
automatically get picked up and installed during `tutor launch` since it follows
the `platform-plugin-*` pattern.

After that any changes made to code here should cause an automatic reload.

Deploying
*********

Simply adding this to the list of installed packages in
`OPENEDX_EXTRA_PIP_REQUIREMENTS` should be sufficient.


License
*******

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to discuss your new feature idea with the maintainers before beginning development
to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@opencraft.com.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/platform-plugin-lti-launch-monitor.svg
    :target: https://pypi.python.org/pypi/platform-plugin-lti-launch-monitor/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/open-craft/platform-plugin-lti-launch-monitor/actions/workflows/ci.yml/badge.svg?branch=main
    :target: https://github.com/open-craft/platform-plugin-lti-launch-monitor/actions/workflows/ci.yml
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/open-craft/platform-plugin-lti-launch-monitor/coverage.svg?branch=main
    :target: https://codecov.io/github/open-craft/platform-plugin-lti-launch-monitor?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/platform-plugin-lti-launch-monitor/badge/?version=latest
    :target: https://docs.openedx.org/projects/platform-plugin-lti-launch-monitor
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/platform-plugin-lti-launch-monitor.svg
    :target: https://pypi.python.org/pypi/platform-plugin-lti-launch-monitor/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/open-craft/platform-plugin-lti-launch-monitor.svg
    :target: https://github.com/open-craft/platform-plugin-lti-launch-monitor/blob/main/LICENSE.txt
    :alt: License

.. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
