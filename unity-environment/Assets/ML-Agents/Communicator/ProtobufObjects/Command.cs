// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: communicator/command.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace MLAgents.Communicator {

  /// <summary>Holder for reflection information generated from communicator/command.proto</summary>
  public static partial class CommandReflection {

    #region Descriptor
    /// <summary>File descriptor for communicator/command.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static CommandReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Chpjb21tdW5pY2F0b3IvY29tbWFuZC5wcm90bxIMY29tbXVuaWNhdG9yKigK",
            "B0NvbW1hbmQSCAoEU1RFUBAAEgkKBVJFU0VUEAESCAoEUVVJVBACQhiqAhVN",
            "TEFnZW50cy5Db21tdW5pY2F0b3JiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(new[] {typeof(global::MLAgents.Communicator.Command), }, null));
    }
    #endregion

  }
  #region Enums
  public enum Command {
    [pbr::OriginalName("STEP")] Step = 0,
    [pbr::OriginalName("RESET")] Reset = 1,
    [pbr::OriginalName("QUIT")] Quit = 2,
  }

  #endregion

}

#endregion Designer generated code
