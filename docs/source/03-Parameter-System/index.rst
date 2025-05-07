Understanding CDKit's Parameter System
==============================================================================
The CDKit Parameter System addresses common challenges in AWS CDK development by providing a more structured and type-safe approach to manage construct and stack parameters. This documentation compares the traditional approach with CDKit's enhanced parameter management system.


The Problem with Traditional CDK Parameter Management
------------------------------------------------------------------------------
Traditional CDK stack implementation requires manually defining all parameters in the constructor, managing defaults, and handling type safety yourself. This approach becomes unwieldy as applications grow more complex.

Let's examine the traditional approach:

.. literalinclude:: ./example_the_old_way.py
   :language: python
   :linenos:

In this traditional approach, several issues emerge:

1. **Repetitive Parameter Definitions**: Each subclass needs to redefine all parameters in the constructor signature.
2. **Loss of Type Information**: Using `**kwargs` loses type hints and IDE completion support.
3. **Manual Validation Required**: You must manually validate required parameters.
4. **Poor Maintainability**: Adding or changing parameters requires updates in multiple places.
5. **Inconsistent Parameter Handling**: Different developers may implement parameter validation differently.


CDKit's Enhanced Parameter System
------------------------------------------------------------------------------
CDKit solves these problems with a structured parameter system built on Python dataclasses:

.. literalinclude:: ./example_the_new_way.py
   :language: python
   :linenos:


Benefits of CDKit's Parameter System
------------------------------------------------------------------------------
1. Type Safety and IDE Support
    - All parameters are strongly typed with proper annotations
    - Full IDE autocompletion for parameters
    - Type checking catches errors at development time
2. Centralized Parameter Definition
    - Parameters are defined once in the dataclass
    - Changes to parameters happen in one place
    - Consistent parameter handling across the project
3. Built-in Parameter Validation
    - Required parameters are clearly marked (`REQ`)
    - Optional parameters have explicit defaults (`OPT`)
    - Validation happens automatically when parameters are instantiated


4. Cleaner Stack Implementation
------------------------------------------------------------------------------
- Stack implementation focuses on business logic, not parameter handling
- Constructor is simplified to just `scope` and `params`
- Self-documenting parameter organization


5. Easy Extension
------------------------------------------------------------------------------
- New parameters can be added by extending the parameter dataclass
- Parameter inheritance mirrors the stack inheritance hierarchy
- Common parameters are inherited, specific ones are added


Summary
------------------------------------------------------------------------------
The CDKit parameter system transforms AWS CDK development by providing a more structured, type-safe, and maintainable approach to parameter management. By leveraging Python dataclasses, it eliminates repetitive code, improves type safety, and ensures consistent parameter handling across your CDK applications.

.. seealso::

    See :class:`~cdkit.base.BaseConstruct`, :class:`~cdkit.base.BaseStack`, it only takes one customizable :class:`~cdkit.params.ConstructParams` and :class:`~cdkit.params.StackParams` to create a stack.

This approach significantly reduces boilerplate code while improving code quality and maintainability.
