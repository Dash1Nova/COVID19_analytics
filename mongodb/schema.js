use("covid_project");

db.createCollection("comments", {
  validator: {
    $jsonSchema: {
      bsonType: "object",

      required: ["country", "date", "comment", "created_by"],

      properties: {
        country: {
          bsonType: "string",
          description: "Country name",
        },

        date: {
          bsonType: "date",
          description: "COVID data date",
        },

        comment: {
          bsonType: "string",
          description: "User or analyst annotation",
        },

        created_by: {
          bsonType: "string",
          description: "Author of the comment",
        },

        tags: {
          bsonType: "array",
          items: {
            bsonType: "string",
          },
          description: "Optional tags",
        },

        created_at: {
          bsonType: "date",
          description: "Comment creation timestamp",
        },
      },
    },
  },
});

db.createCollection("external_information", {
  validator: {
    $jsonSchema: {
      bsonType: "object",

      required: ["country", "source_name", "title", "url"],

      properties: {
        country: {
          bsonType: "string",
          description: "Country name",
        },

        source_name: {
          bsonType: "string",
          description: "Source of information",
        },

        title: {
          bsonType: "string",
          description: "Article title",
        },

        url: {
          bsonType: "string",
          description: "Source URL",
        },

        description: {
          bsonType: "string",
          description: "Short summary",
        },

        publication_date: {
          bsonType: "date",
          description: "Publication date",
        },

        related_metrics: {
          bsonType: "array",
          items: {
            bsonType: "string",
          },
          description: "Metrics mentioned (cases, deaths, etc.)",
        },
      },
    },
  },
});
