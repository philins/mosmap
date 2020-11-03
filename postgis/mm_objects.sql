
-- ----------------------------
-- Table structure for mm_objects
-- ----------------------------
DROP TABLE IF EXISTS "public"."mm_objects";
CREATE TABLE "public"."mm_objects" (
  "obj_id" serial,
  "obj_name" varchar(255) COLLATE "pg_catalog"."default",
  "obj_fullname" text COLLATE "pg_catalog"."default",
  "obj_parent_id" int4,
  "obj_geom" "public"."geometry",
  "obj_st_id" int4 NOT NULL,
  "obj_map_id" int4 NOT NULL,
  "obj_obj_id" int4,
  "obj_class_id" int4,
  "obj_prclass_id" int4,
  "floors" varchar(255) COLLATE "pg_catalog"."default",
  "jil" int4
)
;

-- ----------------------------
-- Indexes structure for table mm_objects
-- ----------------------------
CREATE INDEX "cid" ON "public"."mm_objects" USING btree (
  "obj_class_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "geoindex" ON "public"."mm_objects" USING gist (
  "obj_geom" "public"."gist_geometry_ops_2d"
);
CREATE INDEX "mid" ON "public"."mm_objects" USING btree (
  "obj_map_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "oid" ON "public"."mm_objects" USING btree (
  "obj_obj_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "st_id" ON "public"."mm_objects" USING btree (
  "obj_st_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table mm_objects
-- ----------------------------
ALTER TABLE "public"."mm_objects" ADD CONSTRAINT "mm_objects_pkey" PRIMARY KEY ("obj_id", "obj_map_id", "obj_st_id");

